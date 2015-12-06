def main():
    filename = 'file.txt'
    with open(filename, 'r') as data:
        print(data.read())

if __name__ == '__main__':
    main()
