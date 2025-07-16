# AI Agent (Boot.Dev)

Following the instructions of the Boot.Dev website this thing was made.

## TODO:
- [ ] Fix the warning: > Warning: there are non-text parts in the response: ['function_call'],returning concatenated text result from text parts,check out the non text parts for full response from model.
- [ ] Before getting it to properly work, the AI was showing its train of thought. E.g.

uv run main.py "how does the calculator render results to the console?"
Called function: get_files_info({})

I need to inspect the calculator's code to understand how it renders results to the console. I'll start by listing the files in the directory to identify the relevant files. Then, I'll read the contents of those files to understand the rendering logic.

Called function: get_file_content({'file_path': './calculator/main.py'})

Okay, the files in the `calculator` directory are `main.py`, `pkg`, `lorem.txt`, `tests.py`, and `README.md`. `main.py` seems like the most relevant file for understanding how the calculator renders results. I'll read the contents of `main.py` to understand its rendering logic.


Called function: get_file_content({'file_path': 'main.py', 'working_directory': './calculator'})

My apologies, it seems I had some trouble accessing the file. Let's try this again.


Called function: get_files_info({'directory': './calculator/pkg'})

Okay, I've got the content of `main.py`. It looks like the calculator uses a `render` function from the `pkg.render` module to format the output. The `render` function takes the expression and the result as input and returns a string, which is then printed to the console.

To understand exactly *how* the result is rendered, I need to examine the `pkg.render` module. I'll start by listing the files inside the `pkg` directory.


Called function: get_files_info({'directory': './calculator'})

Ah, it seems that 'pkg' was a file and not a directory. I will need to change my approach. I'll list the files from the root again to confirm.


Called function: get_files_info({})

I seem to be having some issues navigating the directory structure. I will start from the base directory, list the files, and then proceed from there.


Called function: get_files_info({'working_directory': './calculator', 'directory': 'pkg'})

Okay, `pkg` is indeed a directory. I apologize for the previous errors. Let's list the contents of the `pkg` directory.


Called function: get_file_content({'file_path': 'pkg/render.py', 'working_directory': './calculator'})

Okay, the `pkg` directory contains `render.py`, `calculator.py`, `morelorem.txt`, and `__pycache__`. Since `main.py` imports `render` from `pkg.render`, I need to read `render.py` to understand how the rendering happens.

~~~ Stops here since it just stops and I couldn't figure out why ~~~

I truely like how the AI gets confused, and that I can see it. Makes it feel real and goofy.
I want to properly implement it one day. 