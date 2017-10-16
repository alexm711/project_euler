
from importlib import import_module
from itertools import product

zero21 = import_module('021')


def gen_abundent_numbers(n,abundent_numbers):
	for i in range(n+1):
		if sum(zero21.proper_divisors(i)) > i:
			abundent_numbers.add(i)

def cannot_be_written_set(n=28123):
	cannot_set = set(range(1,n))
	abundent_numbers_set = set()
	gen_abundent_numbers(n,abundent_numbers_set)
	for i,j in product(abundent_numbers_set,abundent_numbers_set):
		if i+j in cannot_set:
			cannot_set.remove(i+j)
	return cannot_set



assert sum(zero21.proper_divisors(28)) == 28, zero21.proper_divisors(28)
answer = sum(cannot_be_written_set(n=28123))
assert answer == 4179871, answer
