# Quadratic primes

from math import sqrt
from itertools import product

prime_array = [2,3]

def gen_primes(limit):
	for x in range(prime_array[-1]+1 ,limit+3):
		if is_prime(x):
			prime_array.append(x)
	# print(prime_array)

def is_prime(num):
	limit = int(sqrt(num))
	if limit > prime_array[-1]:
		gen_primes(num)
	for x in prime_array:
		if x > limit:
			return True
		if num%x == 0:
			return False
	else:
		return True

def longest_stretch(a,b):
	curr_prime = b
	if not is_prime(b):
		return 0
	i = 1
	curr_prime = i + a*i + b
	while curr_prime >0 and is_prime(curr_prime):
		i+=1
		curr_prime = i**2 + a*i + b
	return i




def main():
	assert longest_stretch(1,41) == 40, longest_stretch(1,41)
	assert longest_stretch(-79,1601) == 80, longest_stretch(-79,1601)

	max_primes,max_prod = 0, 0
	for a,b in product(range(-999,1000),range(0,1001)):
		if longest_stretch(a,b) > max_primes:
			max_primes = longest_stretch(a,b)
			max_prod = a*b
	# print(max_prod)
	assert -59231 == max_prod

if __name__ == '__main__':
	main()
