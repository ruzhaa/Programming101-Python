def sum(digits):
    result = 0
    for num in range(0, len(digits)):
        result += digits[num]
    return result

print(sum([1,3,5]))
