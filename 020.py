# Factorial digit sum
from math import factorial

def factorial_digit_sum(n):
	str_fact = str(factorial(n))
	return sum(int(d) for d in str_fact)

assert factorial_digit_sum(10) == 27, factorial_digit_sum(10) 
print(factorial_digit_sum(100))
