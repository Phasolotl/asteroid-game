import os
from functions.config import MAX_CHAR



def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(full_path)

        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file_path, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHAR:
                file_content_string = (
                        file_content_string[:MAX_CHAR]
                        + f'[...File "{file_path}" truncated at 10000 characters]'
                )
        return file_content_string

    except Exception as e:
        return f"Error: {e}"