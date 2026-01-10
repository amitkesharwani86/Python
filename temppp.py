import openai

# Set up your OpenAI API key
openai.api_key = "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"

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)