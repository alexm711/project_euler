# Amicable numbers
from math import sqrt

def proper_divisors(n):
	div = []
	upper = int(sqrt(n)) 
	for i in range(1 , upper +1):
		if n % i == 0:
			if i ** 2 == n or i == 1:
				div.append(i)
			else:
				div.extend([i,n//i])
	return div

def d(n):
	return sum(proper_divisors(n))

def amicable_numbers(max_n):
	Dict = {}
	total = 0
	for n in range(1,max_n):
		num = d(n)
		if num in Dict and d(num) == n and num != n:
			total+= num + n
		else:
			Dict[n] = num
	return total

def main():
	assert sorted(proper_divisors(220)) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
	assert sorted(proper_divisors(284)) == [1, 2, 4, 71, 142]
	assert d(284) == 220
	assert d(220) == 284

	max_n = 10000
	assert 31626 == amicable_numbers(max_n)


if __name__ == "__main__":
	main()