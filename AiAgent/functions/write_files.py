import os


def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(full_path)

        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(abs_file_path):
            parent_direct = os.path.dirname(abs_file_path)
            os.makedirs(parent_direct, exist_ok=True)

        with open(abs_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as err:
        return f"Error: {err}"