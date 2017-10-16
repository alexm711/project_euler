# Prime permutations

from importlib import import_module
zero35 = import_module('035')

from itertools import permutations


def arith_sequence(prime,prime_set):
	perms = [int(''.join(p)) for p in permutations(str(prime))]
	perms = sorted(list(set([p for p in perms if p in prime_set])))

	if len(perms)<3:
		return 0

	for i in range(len(perms)-2):
		for j in range(i+1,len(perms)-1):
			for k in range(j+1,len(perms)):
				if perms[j]-perms[i] == perms[k]-perms[j]:
					return perms[i], perms[j], perms[k]
	return 0


def main():
	primes = zero35.primesfrom2to(10000)

	for i,prime in enumerate(primes):
		if prime >= 1000:
			primes = primes[i:]
			break

	prime_set = set(primes)
	sequences = set()
	for prime in primes:
		sequences.add(arith_sequence(prime,prime_set))

	print(sequences)
	# (2969, 6299, 9629)

if __name__ == '__main__':
	main()
