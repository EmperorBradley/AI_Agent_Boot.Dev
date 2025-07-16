#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
#from functions.write_file import write_file
from functions.run_python_file import run_python_file

if __name__ == "__main__":
    print("Test 1:")
    print(run_python_file("calculator", "main.py"))

    print("Test 2:")
    print(run_python_file("calculator", "tests.py"))

    print("Test 3:")
    print(run_python_file("calculator", "../main.py"))

    print("Test 4:")
    print(run_python_file("calculator", "nonexistent.py"))

    # print("Test 1:")
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    # print("Test 2:")
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    # print("Test 3:")
    # print(write_file("calculator", "/tmp/temp.txt", "this shoud not be allowed"))

    # for testing get_file_content
    # print("Test 1:")
    # print(get_file_content("calculator", "lorem.txt"))

    # print("Test 2:")
    # print(get_file_content("calculator", "main.py"))

    # print("Test 3:")
    # print(get_file_content("calculator", "pkg/calculator.py"))

    # print("Test 4:")
    # print(get_file_content("calculator", "/bin/cat"))

    # for testing get_files_info
    # print("Test 1:")
    # print(get_files_info("calculator", "."))
    
    # print("Test 2:")
    # print(get_files_info("calculator", "pkg"))

    # print("Test 3:")
    # print(get_files_info("calculator", "/bin"))
    
    # print("Test 4:")
    # print(get_files_info("calculator", "../"))
