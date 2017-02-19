from task01 import to_digits
from task01 import palindrome
import copy


def is_number_balanced(n):
    firs_list = to_digits(n)
    sum_one = 0
    sum_two = 0
    if len(str(n)) % 2 == 0:
        sum_one = sum([int(str(firs_list[i]))
                       for i in range(0, len(str(n)) // 2)])
        sum_two = sum([int(str(firs_list[i]))
                       for i in range(len(str(n)) // 2, len(str(n)))])
    else:
        sum_one = sum([int(str(firs_list[i]))
                       for i in range(0, len(str(n)) // 2)])
        sum_two = sum([int(str(firs_list[i]))
                       for i in range((len(str(n)) + 1) // 2, len(str(n)))])
    return sum_one == sum_two


# task02 - 2.1/2.2
def is_increasing(seq):
    start = 0
    next = 1
    while next < len(seq):
        if seq[start] >= seq[next]:
            return False
        else:
            start += 1
            next += 1
    return True


def is_decreasing(seq):
    start = 0
    next = 1
    while next < len(seq):
        if seq[start] <= seq[next]:
            return False
        else:
            start += 1
            next += 1
    return True


def get_largest_palindrome(n):
    n -= 1
    while n >= 0:
        if palindrome(n):
            break
        n -= 1
    return n


def prime_numbers(n):
    prime = set()
    elements = []
    for num in range(2, n + 1):
        if num in elements:
            continue
        for i in range(num * 2, n + 1, num):
            elements.append(i)
        prime.add(num)
    return prime


def is_anagram(a, b):
    return sorted(str(a).lower()) == sorted(str(b).lower())


def birthday_ranges(birthdays, ranges):
    counter = 0
    result = []
    for r in range(0, len(ranges)):
        for day in range(0, len(birthdays)):
            if birthdays[day] >= ranges[r][0] and birthdays[day] <= ranges[r][1]:
                counter += 1
        result.append(counter)
        counter = 0
    return result


def sum_matrix(m):
    return sum(m[row] for row in m)

# matrix bombing:
