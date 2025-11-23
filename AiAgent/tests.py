from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content


def main():

    result1 = get_file_content("calculator", "main.py")
    result2 = get_file_content("calculator", "pkg/calculator.py")
    result3 = get_file_content("calculator", "/bin/cat")
    result4 = get_file_content("calculator", "pkg/does_not_exist.py")

    print(result1)
    print(result2)
    print(result3)
    print(result4)

if __name__ == "__main__":
    main()
