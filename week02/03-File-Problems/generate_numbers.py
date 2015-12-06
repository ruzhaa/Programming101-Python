import sys
from random import randint


def main():
    data = open('numbers.txt', 'r+')
    for num in range(int(sys.argv[2])):
            number = randint(1, 1000)
            data.write(str(number) + " ")
    data.close()


if __name__ == '__main__':
    main()
