from importlib import import_module
zero35 = import_module('035')
import itertools
from math import sqrt

def Goldbach(n,primes):
	i, sqrtn = 1, sqrt(n//2)
	while i <= sqrtn:
		if n-2*(i**2) in primes:
			return True
		i+=1
	return False


def main():
	max_guess = 10000 # 1+2+...+8 = 36, which is divisible by 3, as well as 1+...+9==45
	primes = set(zero35.primesfrom2to(max_guess))
	for n in itertools.count(33):
		if n%2==0 or n in primes:
			continue
		if not Goldbach(n,primes):
			# print(n)
			assert n == 5777
			return

if __name__ == '__main__':
	main()