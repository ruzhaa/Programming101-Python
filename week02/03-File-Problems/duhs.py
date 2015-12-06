import sys
import os


def check(my_path, size_of_files):
    for it in os.listdir(my_path):
        my_path = os.path.join(my_path, it)
        if os.path.isfile(my_path):
            size_of_files += os.path.getsize(my_path)
        elif os.path.isdir(my_path):
            check(my_path, size_of_files)
    return size_of_files


def main():
    my_path = sys.argv[1]
    size_of_files = os.path.getsize(my_path)
    print(check(my_path, size_of_files))


if __name__ == '__main__':
        main()
