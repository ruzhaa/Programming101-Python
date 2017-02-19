# cat2.py
import sys


def main():
    for argument in sys.argv[1:]:
        with open(str(argument), 'r') as data:
            print(data.read())
            print('\n')


if __name__ == '__main__':
    main()
