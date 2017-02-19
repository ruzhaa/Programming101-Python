def to_digits(n):
	result = []
	sum = 0
	for i in str(n):
		sum += fact_digits(int(i))
		result.append(int(i))
	return result
print(sum)



def to_number(digits):
	result = ""
	for i in range(0, len(digits)):
		result += str(digits[i])
	return result

print(to_number([9, 9, 9, 9]))


def fact_digits(n):
	for i in n:
		

