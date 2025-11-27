import os, subprocess


def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(full_path)

        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        completed_process = subprocess.run(["python", abs_file_path, *args],
                       cwd=abs_working_directory,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       timeout=30,
                       text=True)

        if not completed_process.stdout and not completed_process.stderr:
            return f"No output produced."
        result = f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"
        if completed_process.returncode != 0:
            result += f"\nProcess exited with code {completed_process.returncode}"

        return result
    except Exception as e:
        return f"Error: executing Python file: {e}"