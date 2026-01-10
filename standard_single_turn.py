# standard_single_turn.py

from dotenv import load_dotenv
import os
from openai import OpenAI

from system_prompt import system_prompt
from user_prompt import user_prompt


def run():
    load_dotenv()

    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    client = OpenAI(api_key=openai_api_key)

    response = client.responses.create(
        model="gpt-5-nano",
        input=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    print(response.output_text)


if __name__ == "__main__":
    run()

# python standard_single_turn.py