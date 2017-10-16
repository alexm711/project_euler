
from importlib import import_module
from itertools import count
zero35 = import_module('035')




def prime_diagonals_over_diagonals_iteratively(primes,max_prime,stopping_fraction):
	num_primes, num_diagonals = 0, 1
	prev_end = 1
	for i in count(1):

		diagonals = [prev_end + (2*j)*i for j in range(1,5)]
		prev_end = diagonals[-1]

		assert prev_end < max_prime, "need more primes"

		num_primes+=sum(d in primes for d in diagonals)
		num_diagonals+=4

		if i==3:
			assert num_primes == 8 and num_diagonals == 13
			
		if  num_primes/num_diagonals < stopping_fraction:
			return 1 + 2*i


def main():
	max_prime = 700000000
	primes = set(zero35.primesfrom2to(max_prime))
	assert prime_diagonals_over_diagonals_iteratively(primes,max_prime,1/10) == 26241 # 688590081 elements is massive!



if __name__ == '__main__':
	main()