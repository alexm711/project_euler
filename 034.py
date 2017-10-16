
# Observation: it's impossible for a number with more than 7 digits to have it's 
# digit factorial equal itself, considering how 9!*7 == 2540160 and 9!*8 == 2903040

from math import factorial

d = {
'0' : factorial(0),
'1' : factorial(1),
'2' : factorial(2),
'3' : factorial(3),
'4' : factorial(4),
'5' : factorial(5),
'6' : factorial(6),
'7' : factorial(7),
'8' : factorial(8),
'9' : factorial(9),
}


def equals_digit_fact(num,print_num=False):
	if print_num:
		print(sum( d[digit] for digit in str(num)))
	return num == sum( d[digit] for digit in str(num))

def gen_equal_digit_fact():
	l = []
	for i in range(3,2000000):
		if i % 10000 == 0:
			print(i)
		if equals_digit_fact(i):
			l.append(i)
	return l

assert equals_digit_fact(145) 
nums = gen_equal_digit_fact()
assert sum(nums) == 40730