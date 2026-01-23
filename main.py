# main.py

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

        response = client.responses.create(
            model=model,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
        )

        print(response.output_text)
        print()


if __name__ == "__main__":
    main()



# python main.py