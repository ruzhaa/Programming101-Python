# cat2.py
import sys


def main():
    res = ''
    for argument in sys.argv[1:]:
        with open(str(argument), 'r') as data:
            res += data.read()
    print(res)

if __name__ == '__main__':
    main()
