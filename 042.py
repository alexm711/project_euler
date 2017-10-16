# Coded triangle numbers

from importlib import import_module
zero22 = import_module('022')

def t_n(n):
	return n * (n+1)//2

def gen_tri_numbers(val):
	n = len(tri_set)
	tn = t_n(n)
	while tn < val:
		n+=1		
		tn = t_n(n)
		tri_set.add(tn)


def is_triangle_word(string):
	val = zero22.word_score(string)
	if val > t_n(len(tri_set)):
		gen_tri_numbers(val)
	return val in tri_set


tri_set = set()

def main():
	with open('042.txt') as f:
		words = f.read().split(',')


	assert zero22.word_score("SKY") == 55
	assert is_triangle_word("SKY")

	total = sum(is_triangle_word(word.strip("\"")) for word in words)
	assert total  == 162


if __name__ == '__main__':
	main()