# Pandigital prime
from importlib import import_module
zero35 = import_module('035')
zero32 = import_module('032')

def main():
	max_num = 7654321 # 1+2+...+8 = 36, which is divisible by 3, as well as 1+...+9==45
	primes = set(zero35.primesfrom2to(max_num))

	max_prime = max(prime for prime in primes if zero32.is_pandigital(str(prime)))	
	assert max_prime == 7652413

if __name__ == '__main__':
	main()
