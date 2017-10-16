# Consecutive prime sum

from importlib import import_module
zero35 = import_module('035')
import itertools


def test_longest_sum(limit):
	primes = zero35.primesfrom2to(limit)
	prime_set = set(primes)
	max_length, max_prime = 1,0

	for i in range(len(primes)):
		curr_sum = sum(primes[i:i+max_length])
		for j in range(i+max_length,len(primes)):
			curr_sum += primes[j]
			if curr_sum in prime_set:
				max_length, max_prime = j-i+1, curr_sum
			if curr_sum >= limit:
				break
	return max_prime




def main():
	assert test_longest_sum(100) == 41
	assert test_longest_sum(1000) == 953
	assert test_longest_sum(1000000) == 997651

if __name__ == '__main__':
	main()