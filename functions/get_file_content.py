import os
from LIMITS import READ_LIMIT
from google.genai import types

def get_file_content(working_directory: str, file_path: str):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
    except Exception as E:
        return f"An error has occurred: {E}"
    
    if os.path.abspath(working_directory) not in full_path:
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
    
    if not os.path.isfile(full_path):
        return f"Error: File is not found or is not a regular file: \"{file_path}\""
    
    contents = ""
    with open(full_path, "r") as file:
        contents = file.read(READ_LIMIT)
    
    if os.path.getsize(full_path) > READ_LIMIT:
        contents += f"\n[...File \"{file_path}\" truncated at {READ_LIMIT} characters]"
    return contents

# telling the AI what this function is, what it does, args it takes.
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the contents of the file provided.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, list files in the working directory itself.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file name of the file to get contents of."
            )
        },
    ),
)