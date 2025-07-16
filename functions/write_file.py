import os 

def write_file(working_directory: str, file_path: str, content: str):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
    except Exception as E:
        return f"An error has occurred: {E}"
    
    if os.path.abspath(working_directory) not in full_path:
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
    
    try:
        with open(full_path, "w") as file:
            file.write(content)
    
        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error writing to file: {e}"

from google.genai import types
# telling the AI what this function is, what it does, args it takes.
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to provided file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, list files in the working directory itself.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file name of the file to be written to."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Contents to be written to the file."
            )
        },
    ),
)