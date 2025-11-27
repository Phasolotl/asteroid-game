from google.genai import types

def schematic_write_file():
    schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Write content or files in the specified file or directory, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file to write to, relative to the working directory.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content to write into the file, relative to the working directory.",
                )
            },
        ),
    )
    return schema_write_file

def schematic_files_info():
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )
    return schema_get_files_info

def schematic_files_content():
    schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Lists the content within a specified file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file to list contents from, relative to the working directory.",
                ),
            },
        ),
    )
    return schema_get_file_content

def schematic_python_file():
    schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Run a specific file in the specified directory, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file to run from, relative to the working directory.",
                ),
            },
        ),
    )
    return schema_run_python_file