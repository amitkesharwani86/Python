import pandas as pd
import numpy as np

# ==========================================================
# SAMPLE DATAFRAME
# ==========================================================

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya", "Neha"],
    "Age": [20, 22, 21, 23],
    "Marks": [85, 90, 95, 88],
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 60000, 70000, 55000]
})

print("\nORIGINAL DATAFRAME")
print(df)

# ==========================================================
# BASIC INFORMATION
# ==========================================================

print("\nHEAD")
print(df.head())

print("\nTAIL")
print(df.tail())

print("\nINFO")
print(df.info())

print("\nDESCRIBE")
print(df.describe())

print("\nSHAPE")
print(df.shape)

print("\nCOLUMNS")
print(df.columns)

print("\nDTYPES")
print(df.dtypes)

# ==========================================================
# COLUMN SELECTION
# ==========================================================

print("\nNAME COLUMN")
print(df["Name"])

print("\nMULTIPLE COLUMNS")
print(df[["Name", "Marks"]])

# ==========================================================
# ROW SELECTION
# ==========================================================

print("\nLOC[0]")
print(df.loc[0])

print("\nILOC[0]")
print(df.iloc[0])

print("\nROWS 0:3")
print(df.iloc[0:3])

# ==========================================================
# FILTERING
# ==========================================================

print("\nAGE > 21")
print(df[df["Age"] > 21])

print("\nMARKS > 85")
print(df[df["Marks"] > 85])

# ==========================================================
# SORTING
# ==========================================================

print("\nSORT AGE ASC")
print(df.sort_values("Age"))

print("\nSORT MARKS DESC")
print(df.sort_values("Marks", ascending=False))

# ==========================================================
# ADD COLUMN
# ==========================================================

df["Grade"] = ["B", "A", "A+", "A"]

print("\nADD GRADE")
print(df)

# ==========================================================
# UPDATE VALUE
# ==========================================================

df.loc[0, "Marks"] = 100

print("\nUPDATE MARKS")
print(df)

# ==========================================================
# DROP COLUMN
# ==========================================================

print("\nDROP GRADE")
print(df.drop("Grade", axis=1))

# ==========================================================
# MISSING VALUES
# ==========================================================

df2 = pd.DataFrame({
    "Name": ["Amit", None, "Priya"],
    "Marks": [90, np.nan, 85]
})

print("\nDATA WITH NULLS")
print(df2)

print("\nISNULL")
print(df2.isnull())

print("\nNULL COUNT")
print(df2.isnull().sum())

print("\nFILL NULL")
print(df2.fillna(0))

# ==========================================================
# STRING FUNCTIONS
# ==========================================================

print("\nLOWER")
print(df["Name"].str.lower())

print("\nUPPER")
print(df["Name"].str.upper())

print("\nCONTAINS A")
print(df["Name"].str.contains("A"))

# ==========================================================
# NUMERICAL FUNCTIONS
# ==========================================================

print("\nSUM")
print(df["Marks"].sum())

print("\nMEAN")
print(df["Marks"].mean())

print("\nMEDIAN")
print(df["Marks"].median())

print("\nMAX")
print(df["Marks"].max())

print("\nMIN")
print(df["Marks"].min())

print("\nSTD")
print(df["Marks"].std())

# ==========================================================
# UNIQUE VALUES
# ==========================================================

print("\nUNIQUE DEPARTMENTS")
print(df["Department"].unique())

print("\nVALUE COUNTS")
print(df["Department"].value_counts())

# ==========================================================
# GROUPBY
# ==========================================================

print("\nGROUPBY MEAN SALARY")
print(df.groupby("Department")["Salary"].mean())

print("\nGROUPBY MAX MARKS")
print(df.groupby("Department")["Marks"].max())

# ==========================================================
# MERGE
# ==========================================================

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Salary": [1000, 2000, 3000]
})

print("\nMERGE")
print(pd.merge(df1, df2, on="ID"))

# ==========================================================
# CONCAT
# ==========================================================

print("\nCONCAT ROWS")
print(pd.concat([df1, df1]))

# ==========================================================
# APPLY
# ==========================================================

print("\nAPPLY +5")
print(df["Marks"].apply(lambda x: x + 5))

# ==========================================================
# DATE FUNCTIONS
# ==========================================================

dates = pd.to_datetime([
    "2025-01-10",
    "2025-02-15",
    "2025-03-20"
])

print("\nYEAR")
print(dates.year)

print("\nMONTH")
print(dates.month)

print("\nDAY")
print(dates.day)

# ==========================================================
# DATA TYPE CONVERSION
# ==========================================================

print("\nFLOAT")
print(df["Age"].astype(float))

# ==========================================================
# SAMPLING
# ==========================================================

print("\nSAMPLE 2")
print(df.sample(2))

# ==========================================================
# CORRELATION
# ==========================================================

print("\nCORRELATION")
print(df[["Age", "Marks", "Salary"]].corr())

# ==========================================================
# RANKING
# ==========================================================

print("\nRANK")
print(df["Marks"].rank())

# ==========================================================
# WINDOW FUNCTIONS
# ==========================================================

print("\nROLLING MEAN")
print(df["Marks"].rolling(2).mean())

# ==========================================================
# SHIFTING
# ==========================================================

print("\nSHIFT")
print(df["Marks"].shift(1))

print("\nDIFF")
print(df["Marks"].diff())

# ==========================================================
# ONE HOT ENCODING
# ==========================================================

print("\nGET DUMMIES")
print(pd.get_dummies(df["Department"]))

# ==========================================================
# REPLACE
# ==========================================================

print("\nREPLACE IT WITH TECH")
print(df.replace("IT", "TECH"))

# ==========================================================
# MELT
# ==========================================================

print("\nMELT")
print(df.melt())

# ==========================================================
# BOOLEAN OPERATIONS
# ==========================================================

print("\nWHERE > 90")
print(df["Marks"].where(df["Marks"] > 90))

# ==========================================================
# SEARCHING
# ==========================================================

print("\nISIN")
print(df["Department"].isin(["IT"]))

# ==========================================================
# STATISTICS
# ==========================================================

print("\nSKEW")
print(df["Marks"].skew())

print("\nKURTOSIS")
print(df["Marks"].kurt())

print("\nQUANTILE")
print(df["Marks"].quantile(0.25))

# ==========================================================
# NUMPY CONVERSION
# ==========================================================

print("\nTO NUMPY")
print(df.to_numpy())

# ==========================================================
# MEMORY USAGE
# ==========================================================

print("\nMEMORY")
print(df.memory_usage())

# ==========================================================
# COPY
# ==========================================================

copy_df = df.copy()

print("\nCOPY")
print(copy_df)