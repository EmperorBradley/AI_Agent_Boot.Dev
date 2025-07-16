import os
from google.genai import types

def get_files_info(working_directory: str, directory="."):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, directory))
    except Exception as E:
        return f"An error has occurred: {E}"
    
    if os.path.abspath(working_directory) not in full_path:
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    
    if not os.path.isdir(full_path):
        return f"Error: \"{directory}\" is not a directory"

    #go through each item in the directory
    items = os.listdir(full_path)
    returnstring = "Result for current directory:\n"
    for item in items:
        itempath = full_path + '/' + item
        returnstring += f"- {item}: file_size={os.path.getsize(itempath)} bytes, is_dir={os.path.isdir(itempath)}\n"
    return returnstring

# telling the AI what this function is, what it does, args it takes.
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, list files in the working directory itself.",
            ),
        },
    ),
)
