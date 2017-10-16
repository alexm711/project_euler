
from math import sqrt



def is_prime(num,prime_array):
	limit = int(sqrt(num)) 
	for x in prime_array:
		if x > limit:
			return True
		if num%x == 0:
			return False

def get_primes(max_n):
	prime_array = [2]
	for number in range(3,max_n,2):
		if is_prime(number,prime_array):
			prime_array.append(number)
	return prime_array

assert sum(get_primes(10)) == 17, get_primes(10)
print(get_primes(10))
print(sum(get_primes(2000000)))