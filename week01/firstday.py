def sum_of_digits(n):
    n = abs(n)
    count = 0
    for i in str(n):
        count += int(i)
    return count


def to_digits(n):
    result = []
    for i in str(n):
        result.append(int(i))
    return result


def to_number(digits):
    result = ""
    for i in digits:
        result += str(i)
    return int(result)


def fact_digits(n):
    result = 0
    current_result = 1
    for num in str(n):
        for i in range(1, int(num) + 1):
            current_result *= i
        result += current_result
        current_result = 1
    return result


def fibonacci(n):
    result = []
    a, b = 1, 1
    for i in range(0, n):  # while len(result) < n
        result.append(a)
        a, b = b, a + b
    return result


def fib_number(n):
    result = ""
    a, b = 1, 1
    for i in range(0, n):
        result += str(a)
        a, b = b, a + b
    return int(result)


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
