#!/usr/bin/env python3
"""
Spam Email Classifier (TF-IDF + Logistic Regression)

Usage:
  # 1) Train on your dataset (CSV with columns: text,label)
  python spam_classifier.py train --data emails.csv --model spam_model.joblib

  # 2) Evaluate on a held-out test split (done automatically during train)

  # 3) Predict a single email text
  python spam_classifier.py predict --model spam_model.joblib --text "Congratulations! You've won a prize"

  # 4) Predict a file with one email per line
  python spam_classifier.py batch --model spam_model.joblib --input emails_to_check.txt --output preds.csv

Dataset format:
  - CSV with columns:
      text  -> the email body/subject as string
      label -> "spam"/"ham" OR 1/0
"""

import argparse
import os
import sys
import json
import numpy as np
import pandas as pd
from typing import Tuple
from joblib import dump, load

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (classification_report, confusion_matrix,
                             roc_auc_score, roc_curve, accuracy_score)
from sklearn.utils.class_weight import compute_class_weight


def load_dataset(path: str) -> Tuple[pd.Series, pd.Series]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)
    needed = {"text", "label"}
    if not needed.issubset(set(df.columns)):
        raise ValueError(f"CSV must have columns {needed}, got {list(df.columns)}")

    # Normalize labels to 0 (ham) / 1 (spam)
    y_raw = df["label"]
    if y_raw.dtype == object:
        y = y_raw.str.strip().str.lower().map({"spam": 1, "ham": 0})
        if y.isna().any():
            # Try interpreting numeric strings
            y = y_raw.astype(str).str.strip().map({"1": 1, "0": 0, "spam": 1, "ham": 0})
    else:
        y = (y_raw.astype(int) > 0).astype(int)

    if y.isna().any():
        bad = df[y.isna()]
        raise ValueError(
            "Could not parse some labels to 0/1 or spam/ham.\n"
            f"Offending rows:\n{bad.head()}"
        )
    X = df["text"].astype(str).fillna("")
    return X, y

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.98,
    strip_accents="unicode"
)

def build_pipeline() -> Pipeline:
    """
    TF-IDF (1-2 grams) + Logistic Regression with class_weight balanced.
    Works well for spam with speed + accuracy.
    """
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.98,
        strip_accents="unicode"
    )
    clf = LogisticRegression(
        max_iter=2000,
        n_jobs=None,
        class_weight="balanced",
        solver="lbfgs"
    )
    pipe = Pipeline([
        ("tfidf", vectorizer),
        ("clf", clf),
    ])
    return pipe


def evaluate(y_true, y_proba, y_pred, label_names=("ham", "spam")) -> dict:
    """
    Compute metrics and return as dict (also prints a concise report).
    """
    try:
        auc = roc_auc_score(y_true, y_proba)
    except Exception:
        auc = float("nan")

    acc = accuracy_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    report = classification_report(
        y_true, y_pred, target_names=label_names, digits=4
    )
    print("\n=== Evaluation ===")
    print(f"Accuracy : {acc:.4f}")
    if not np.isnan(auc):
        print(f"ROC AUC  : {auc:.4f}")
    print("Confusion Matrix [rows=true ham,spam; cols=pred ham,spam]:")
    print(cm)
    print("\nClassification Report:")
    print(report)

    return {
        "accuracy": acc,
        "roc_auc": auc,
        "confusion_matrix": cm.tolist(),
        "report": report
    }


def cmd_train(args):
    X, y = load_dataset(args.data)

    # Train/validation split (stratified)
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=args.test_size, random_state=42, stratify=y
    )

    # Optional: print class balance
    counts = pd.Series(y_tr).value_counts().sort_index()
    print("Train class counts (0=ham,1=spam):")
    print(counts.to_dict())

    # Build & train
    pipe = build_pipeline()
    pipe.fit(X_tr, y_tr)

    # Evaluate
    if hasattr(pipe.named_steps["clf"], "predict_proba"):
        y_prob = pipe.predict_proba(X_te)[:, 1]
    else:
        # Fallback: decision_function can be scaled, but for AUC it's fine
        if hasattr(pipe.named_steps["clf"], "decision_function"):
            scores = pipe.named_steps["clf"].decision_function(X_te)
            # min-max to approx [0,1]
            y_prob = (scores - scores.min()) / (scores.max() - scores.min() + 1e-9)
        else:
            y_prob = np.zeros_like(y_te, dtype=float)

    y_pred = pipe.predict(X_te)
    metrics = evaluate(y_te, y_prob, y_pred)

    # Save
    out_path = args.model
    dump({"pipeline": pipe, "metrics": metrics}, out_path)
    print(f"\nModel saved to: {out_path}")


def load_pipeline(model_path: str) -> Pipeline:
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    bundle = load(model_path)
    pipe = bundle.get("pipeline")
    if pipe is None:
        # Backward-compat: in case only pipeline was saved
        pipe = bundle
    return pipe


def cmd_predict(args):
    pipe = load_pipeline(args.model)
    text = args.text
    if not text:
        print("Provide --text argument.")
        sys.exit(1)

    proba = (
        pipe.predict_proba([text])[:, 1]
        if hasattr(pipe.named_steps["clf"], "predict_proba")
        else None
    )
    pred = pipe.predict([text])[0]
    label = "spam" if pred == 1 else "ham"
    print(json.dumps({
        "prediction": int(pred),
        "label": label,
        "spam_probability": float(proba[0]) if proba is not None else None
    }, indent=2))


def cmd_batch(args):
    pipe = load_pipeline(args.model)
    if not os.path.exists(args.input):
        raise FileNotFoundError(f"Input file not found: {args.input}")

    with open(args.input, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f.readlines() if ln.strip()]

    if not lines:
        print("No lines to classify.")
        sys.exit(0)

    if hasattr(pipe.named_steps["clf"], "predict_proba"):
        probs = pipe.predict_proba(lines)[:, 1]
    else:
        probs = np.full(len(lines), np.nan)

    preds = pipe.predict(lines)
    labels = np.where(preds == 1, "spam", "ham")

    df_out = pd.DataFrame({
        "text": lines,
        "prediction": preds.astype(int),
        "label": labels,
        "spam_probability": probs
    })
    out_path = args.output
    df_out.to_csv(out_path, index=False)
    print(f"Wrote predictions to: {out_path}")
    # Show quick summary
    print(df_out["label"].value_counts())


def build_argparser():
    p = argparse.ArgumentParser(description="Spam Email Classifier")
    sub = p.add_subparsers(dest="command", required=True)

    p_train = sub.add_parser("train", help="Train and evaluate model")
    p_train.add_argument("--data", required=True, help="Path to CSV with text,label")
    p_train.add_argument("--model", default="spam_model.joblib", help="Output model path")
    p_train.add_argument("--test_size", type=float, default=0.2, help="Test split size (0..1)")
    p_train.set_defaults(func=cmd_train)

    p_pred = sub.add_parser("predict", help="Predict a single email text")
    p_pred.add_argument("--model", required=True, help="Path to saved model .joblib")
    p_pred.add_argument("--text", required=True, help="Email content (quote it)")
    p_pred.set_defaults(func=cmd_predict)

    p_batch = sub.add_parser("batch", help="Predict a file, one email per line")
    p_batch.add_argument("--model", required=True, help="Path to saved model .joblib")
    p_batch.add_argument("--input", required=True, help="TXT file, one email per line")
    p_batch.add_argument("--output", default="preds.csv", help="Where to save CSV predictions")
    p_batch.set_defaults(func=cmd_batch)

    return p


def main():
    # Quality-of-life: if user runs without data, create a tiny demo dataset
    if len(sys.argv) == 1:
        demo_csv = "demo_emails.csv"
        if not os.path.exists(demo_csv):
            demo = pd.DataFrame({
                "text": [
                    "Congratulations! You've won a $1000 gift card. Click here to claim now",
                    "Meeting at 3 PM about quarterly report. Please bring the slides.",
                    "Limited time offer!!! Earn money fast by joining our program",
                    "Your Amazon order has been shipped. Track your package here",
                    "URGENT: Your account will be suspended. Verify details immediately",
                    "Lunch tomorrow?",
                ],
                "label": ["spam", "ham", "spam", "ham", "spam", "ham"]
            })
            demo.to_csv(demo_csv, index=False)
            print(f"Created tiny demo dataset: {demo_csv}")
        print(
            "Example commands:\n"
            f"  python {os.path.basename(__file__)} train --data {demo_csv}\n"
            f"  python {os.path.basename(__file__)} predict --model spam_model.joblib --text \"win a prize now\""
        )
        sys.exit(0)

    parser = build_argparser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
