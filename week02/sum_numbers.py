def main():
    with open('numbers.txt', 'r') as data:
        print(sum([int(x) for x in data.read() if x != ' ']))


if __name__ == '__main__':
    main()
