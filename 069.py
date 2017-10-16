

from importlib import import_module

zero35 = import_module('035')
primes = zero35.primesfrom2to(1000000)

def phi(n):
	result = n
	for prime in primes:
		if n<prime:
			break
		if n%prime==0:
			result*=(1 - 1/prime)
	return int(result)

def totient_maximum(limit_n):
	max_n = 1
	for prime in primes:
		if max_n*prime > limit_n:
			return max_n
		max_n*=prime



def main():
	assert phi(9) == 6, phi(9)
	assert phi(4) == 2
	assert phi(6) == 2
	assert totient_maximum(limit_n=10) == 6
	assert totient_maximum(limit_n=10**6) == 510510

if __name__ == '__main__':
	main()