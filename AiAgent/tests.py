from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content
from functions.write_files import write_file


def main():

    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

    print(result1)
    print(result2)
    print(result3)

if __name__ == "__main__":
    main()
