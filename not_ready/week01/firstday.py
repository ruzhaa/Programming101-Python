def sum_of_digits(n):
    return sum([int(i) for i in str(n)])


def to_digits(n):
    result = []
    for i in str(n):
        result.append(int(i))
    return result


def to_number(digits):
    result = ""
    for num in digits:
        result += str(num)
    return result


def fact_digits(num):
    factoriel = 1
    while num != 1:
        factoriel *= num
        num -= 1
    return factoriel


def fibonacci(num):
    result = []
    a, b = 1, 1
    while len(result) < num:
        result.append(a)
        a, b = b, a + b
    return result


def fib_number(num):
    result = ""
    a, b = 1, 1
    for n in range(1, num):
        result += str(a)
        a, b = b, a + b
    return result


# this tasks are refactoring
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def palindrome(n):
    return str(n) == str(n)[::-1]


def count_vowels(string):
    count = 0
    vowels_list = "aeyuioAEYUIO"
    for i in range(0, len(string)):
        if string[i] in vowels_list:
            count += 1
    return count


def count_consonants(string):
    count = 0
    consonants_list = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    for i in range(0, len(string)):
        if string[i] in consonants_list:
            count += 1
    return count


def char_histogram(string):
    char_list = {}
    count = 1
    for i in string:
        if i in char_list:
            count += 1
            char_list[i] = count
        else:
            char_list[i] = count
            count = 1
    return char_list
