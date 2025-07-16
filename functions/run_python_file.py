import os
import subprocess
import sys
from google.genai import types

def run_python_file(working_directory: str, file_path: str):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
    except Exception as E:
        return f"An error has occurred: {E}"
    
    if os.path.abspath(working_directory) not in full_path:
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"
    
    if not os.path.exists(full_path):
        return f"Error: File \"{file_path}\" not found."
    
    if not file_path.endswith(".py"):
        return f"Error: \"{file_path}\" is not a Python file."
    
    process = None
    try:
        process = subprocess.run(
            [sys.executable, full_path], 
            text=True, 
            timeout=30, 
            cwd=working_directory, 
            capture_output=True
        )
    except Exception as e:
        return f"Error: executing Python file: {e}"
    return f"""
STDOUT: ---\n{process.stdout}\n---\n
STDERR: ~~~\n{process.stderr}\n~~~\n
Program exited with code {process.returncode}\n
{"No output produced." if len(process.stdout) == 0 else ""}
"""

# telling the AI what this function is, what it does, args it takes.
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the provided python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, list files in the working directory itself.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file name of the Python file to execute."
            )
        },
    ),
)