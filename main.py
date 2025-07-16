import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function
import LIMITS

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

#simple settings dict
settings = {
    "verbose" : False,
    "system_prompt" : """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
""",
}

# hardcoded ai settings
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_write_file,
        schema_get_file_content,
        schema_run_python_file,
    ]
)

# verbose info
AI_info = {
    "prompt_tokens" : 0,
    "response_tokens" : 0,
}

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f"Usage: main.py [Prompt] --verbose")
        sys.exit(1)
    user_prompt = sys.argv[1]
    
    # check for flags
    for flag in sys.argv:
        match flag:
            case "--verbose":
                settings["verbose"] = True
            case _:
                continue
    
    
    # to remember the history of messages
    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    iteration = 0
    while True:
        iteration += 1
        if iteration > LIMITS.AI_ITERATIONS:
            print(f"Maximum iteration reached: {iteration}")
            break
        try:
            response = Ask_AI(client, messages, settings["verbose"])
            if response:
                # print the AI response
                print(response)
                break
        except Exception as e:
            print(f"Error in Ask_AI: {e}")
            return
    
    
    # print extra details
    if settings["verbose"]:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {AI_info['prompt_tokens']}\nResponse tokens: {AI_info['response_tokens']}")


def Ask_AI(client: genai.Client, messages: list[types.Content], verbose: bool):
    try:
        # sends the prompt to the model
        response = client.models.generate_content(
                model='gemini-2.0-flash-001', 
                contents=messages,
                config=types.GenerateContentConfig(
                    system_instruction=settings["system_prompt"],
                    tools=[available_functions],
                )
        )

        # need to iterate over each .candidate and add it to the messages list
        # this adds the AI's response to the conversation. 
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        # print the function calls it made if any
        function_responses = []
        if response.function_calls:
            for call in response.function_calls:
                print(f"Called function: {call.name}({call.args})")
                resp = call_function(call)

                #add the function call to the messages too
                if not resp.parts or not resp.parts[0].function_response:
                    raise Exception("Error: empty function call result")
                
                if settings["verbose"]:
                    print(f"-> {resp.parts[0].function_response}")

                function_responses.append(resp.parts[0])
                
        messages.append(
            types.Content(
                role="tool",
                parts=function_responses
            )
        )
        #AI is finished
        if response.text and not response.function_calls:
            AI_info["prompt_tokens"] = response.usage_metadata.prompt_token_count
            AI_info["response_tokens"] = response.usage_metadata.candidates_token_count
            return response.text
        
        if not function_responses:
            raise Exception("no function responses generated, exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
