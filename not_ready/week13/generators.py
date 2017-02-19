import glob


def chain(iterable_one, iterable_two):
    for elem in iterable_one:
        yield elem
    for item in iterable_two:
        yield item

# print(list(chain(range(0, 4), range(4, 8))))


def compress(iterable, mask):
    for group in zip(iterable, mask):
        if group[1]:
            yield group[0]


# print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))


def cycle(iterable):
    while True:
        for elem in iterable:
            yield elem


class BookReader:
    def __init__(self, my_path):
        self.my_path = my_path + '/*.txt'

    def __iter__(self):
        return self

    def __next__(self):
        path = glob.glob(self.my_path)
        # print(path)
        for book_file in path:
            # print(book_file)
            with open(book_file, 'r') as current_file:
                current_file.readlines()
        # for f in glob.glob(self.my_path):
        #     with open(f, 'r') as my_file:
        #         for line in my_file.readlines():
        #             if line.startswith("#"):
        #                 print(line)
        #             else:
        #                 break
                # print(my_file.readlines())


def next_chapter():
    command = input("For next chapter: 'n' + ENTER > ")
    return command == 'n'


def book_reader():
    my_path = "/home/ruzha/Programming101/week13/Book" + '/*.txt'
    path = glob.glob(my_path)
    for book_file in path:
        with open(book_file, 'r') as current_file:
            list_chapters = current_file.read().split('#')
            for chapter in list_chapters:
                if next_chapter():
                    print(chapter)

test = book_reader()
print(test)
# b = BookReader("/home/ruzha/Programming101/week13/Book")
# f = iter(b)

# while True:
#     next_chapter = input()
#     if next_chapter is 'n':
#         next(f)
# print(b)
# print(BookReader("/home/ruzha/Programming101/week13/Book"))
# book = book_reader("/home/ruzha/Programming101/week13/Book")
