# Truncatable primes
from importlib import import_module
zero35 = import_module('035')

def truncatable(n):
	str_n = str(n)
	for i in range(1,len(str_n)):
		if int(str_n[i:]) not in primes or int(str_n[:i]) not in primes:
			return False
	return True


def find_truncatable_primes():
	trunc_primes =  [prime for prime in primes if truncatable(prime)]
	for elem in [2,3,5,7]:
		trunc_primes.remove(elem)
	assert len(trunc_primes) == 11, trunc_primes
	return trunc_primes

primes = set(zero35.primesfrom2to(1000000))

assert truncatable(3797)
assert  sum(find_truncatable_primes())   == 748317

