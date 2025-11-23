from tabnanny import verbose

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import sys

def main():
    load_dotenv()

    args = sys.argv[1:]
    verbose_is_on = "--verbose" in args
    filtered_prompt = []
    for string in args:
        if not string.startswith("--"):
            filtered_prompt.append(string)

    if not args:
        print("Error: no prompt detected")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(filtered_prompt)
    if verbose_is_on:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose_is_on)


def generate_content(client, messages, verbose_is_on):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if verbose_is_on:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()


