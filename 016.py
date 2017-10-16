def sum_of_digits(n):
	return sum(int(ch) for ch in str(n))

assert sum_of_digits(2**15) == 26
print(sum_of_digits(2**1000))