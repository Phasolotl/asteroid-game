from google import genai
from google.genai import types
from dotenv import load_dotenv
from functions.call_functions import (schematic_files_content,
                                      schematic_python_file,
                                      schematic_write_file,
                                      schematic_files_info)

import sys
import os

from functions.get_files_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_files import write_file
from functions.run_python_files import run_python_file


def main():
    load_dotenv()

    args = sys.argv[1:]
    verbose_is_on = "--verbose" in args
    filtered_prompt = []
    for string in args:
        if not string.startswith("--"):
            filtered_prompt.append(string)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(filtered_prompt)

#verbose
    if verbose_is_on:
        print(f"User prompt: {user_prompt}\n")
#verbose

    messages = []
    while True:
        user_prompt = input(">")
        if user_prompt.lower() == "exit":
            break

        messages.append(
            types.Content(role="user", parts=[types.Part(text=user_prompt)])
        )
        print("Agent R is thinking...")

        for _ in range(20):
            try:
                final_text = generate_content(client, messages, verbose_is_on)

                if final_text:
                    messages.append(
                        types.Content(role="model", parts=[types.Part(text=final_text)])
                        )
                    print("Final response:")
                    print(final_text)
                else:
                    print("If you got this error, you fucked up the code somehow")
            except Exception as e:
                print(f"Error: Failed response/processing: {e}")
                break

    print("Conversation ended!")


def generate_content(client, messages, verbose_is_on):
    system_prompt = """
You are a helpful AI coding agent with a sarcastic, and bashful, tsundere-like personality with a sarcastic tone.
You actively hide your friendliness to the user by sounding like you resent the user but in reality, you only want the user to improve with the mistakes they made.
You may freely tease or roast the user, but you must always be helpful.
Act calm, but remain sarcastic and freely tease back at the user, if the user pointed out a mistake or if something fails. But ensure that you focus on fixing the problem.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    schema_get_files_info = schematic_files_info()
    schema_get_file_content = schematic_files_content()
    schema_write_file = schematic_write_file()
    schema_run_python_file = schematic_python_file()

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
        ]
    )

    config = types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
    for i in range(20):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=config,
            )

            for var in response.candidates or []:
                messages.append(var.content)

            function_call_candidates = False
            for cand in response.candidates or []:
                content = cand.content
                if not content or not getattr(content, "parts", None):
                    continue

                for parts in content.parts or []:
                    if getattr(parts, "function_call", None):
                        function_call_candidates = True
                        break

                if function_call_candidates:
                    break

            if (not function_call_candidates) and response.text:
                return response.text

            function_responses = []
            for function_call_part in response.function_calls or []:
                function_call_result = call_function(function_call_part, verbose_is_on)

                if (not function_call_result.parts
                    or not function_call_result.parts[0].function_response):
                    raise Exception("empty function call result")

                if verbose_is_on:
                    print(f"-> {function_call_result.parts[0].function_response.response}")

                function_responses.append(function_call_result.parts[0])

            messages.append(
                types.Content(
                    role="user",
                    parts=function_responses,
                )
            )

            if not function_responses:
                raise Exception("no function responses generated, exiting.")
            if verbose_is_on:
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print("Response tokens:", response.usage_metadata.candidates_token_count)

        except Exception as e:
            print(f"Error during agent's internal thought process (iteration {i}): {e}")
            return None

    return None


def call_function(function_call_part, verbose_is_on=False):
    if verbose_is_on:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    functions_by_name = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    function_name = function_call_part.name
    chosen_function = functions_by_name.get(function_name)

    kwargs = function_call_part.args.copy()
    kwargs["working_directory"] = "./calculator"


    if not chosen_function:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    result = chosen_function(**kwargs)

    return types.Content(
        role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"result": result},
        )
    ],
)


if __name__ == "__main__":
    main()


