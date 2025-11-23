from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content
from functions.write_files import write_file
from functions.run_python_files import run_python_file

def main():

    result1 = run_python_file("calculator", "main.py")
    result2 = run_python_file("calculator", "main.py")
    result3 = run_python_file("calculator", "main.py", ["3 + 5"])
    result4 = run_python_file("calculator", "tests.py")
    result5 = run_python_file("calculator", "../main.py")
    result6 = run_python_file("calculator", "nonexistent.py")
    result7 = run_python_file("calculator", "lorem.txt")


    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)
    print(result7)

if __name__ == "__main__":
    main()
