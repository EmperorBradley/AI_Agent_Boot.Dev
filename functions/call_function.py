from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
import LIMITS

def call_function(function: types.FunctionCall):


    args = function.args
    args["working_directory"] = LIMITS.WORKING_DIR
    res = None
    match function.name:
        case get_file_content.__name__:
            res = get_file_content(**args)
        case get_files_info.__name__:
            res = get_files_info(**args)
        case run_python_file.__name__:
            res = run_python_file(**args)
        case write_file.__name__:
            res = write_file(**args)
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=(function.name if function.name is not None else "Unknown"),
                        response={"error": f"Unknown function: {function}"}
                    )
                ]
            )
        
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function.name,
                response={"result": res}
            )
        ]
    )