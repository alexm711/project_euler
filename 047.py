# Distinct Prime Factors


from importlib import import_module
from itertools import product, count
zero35 = import_module('035')

def get_prime_factors(n,primes,primes_set):
	curr_n = n
	prime_factors = set()
	prime_i = 0
	while curr_n>1:
		# for prime in primes:
		prime = primes[prime_i]
		assert prime <= curr_n, "factorization error"
		if curr_n/prime%1==0:
			prime_factors.add(prime)
			curr_n/=prime
			continue
		if curr_n in primes_set:
			prime_factors.add(curr_n)
			return prime_factors
		prime_i+=1

	return prime_factors


def get_n_consecutive_primes_of_length_n(n,primes,primes_set):
	counter = 0
	max_prime = max(primes)
	for i in count(3):
		if len(get_prime_factors(i,primes,primes_set))==n:
			counter+=1
		else:
			counter = 0
		if counter==n:
			return i - n + 1
		assert max_prime > i, "primes too small"




def main():
	primes_limit = 10000000
	primes = zero35.primesfrom2to(primes_limit)
	primes_set = set(primes)
	# print(get_prime_factors(14,primes,primes_set))
	assert get_prime_factors(14,primes,primes_set) == {2,7}
	assert get_prime_factors(15,primes,primes_set) == {3,5}

	assert get_prime_factors(644,primes,primes_set) == {2,7,23}
	assert get_prime_factors(645,primes,primes_set) == {3,5,43}
	assert get_prime_factors(646,primes,primes_set) == {2,17,19}

	assert get_n_consecutive_primes_of_length_n(2,primes,primes_set) == 14
	assert get_n_consecutive_primes_of_length_n(3,primes,primes_set) == 644
	print(get_n_consecutive_primes_of_length_n(3,primes,primes_set) )
	print(get_n_consecutive_primes_of_length_n(4,primes,primes_set))





if __name__ == '__main__':
	main()





