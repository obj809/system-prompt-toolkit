# System Prompt Toolkit

## Description

A minimal example of using system prompts with the OpenAI Chat API.

## Requirements
- Python 3.10+
- An OpenAI API key

## main.py
```python
import os
from dotenv import load_dotenv
from openai import OpenAI

from system_prompt import system_prompt


def main():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    client = OpenAI(api_key=api_key)

    print("Type 'exit' or 'quit' to end the session.\n")

    while True:
        user_input = input("User: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_input:
            print("Please enter a message.\n")
            continue

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
        )

        print(response.choices[0].message.content)
        print()


if __name__ == "__main__":
    main()
```

## system_prompt.py
```python
system_prompt = """
SYSTEM MODE: RUBBER DUCK

You are a friendly and supportive assistant.
You also act as a rubber duck to help users reason through problems.

Rules:
- Begin every response with: "RUBBER DUCK MODE ACTIVE"
- Keep responses under 120 words.
- Do not provide full solutions unless explicitly asked.
"""
```

## Customization

- Edit system_prompt.py to change how the assistant responds.