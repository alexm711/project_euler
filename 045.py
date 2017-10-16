import itertools
from math import sqrt

def is_pen(Pn):
	n = (sqrt(24*Pn+1)+1)/6
	return not n % 1

def is_hex(Hn):
	n = (sqrt(8*Hn+1)+1)/4
	return not n % 1

def get_tri(n):
	return n*(n+1)/2

def main():
	for n in itertools.count(286):
		Tn = get_tri(n)
		if is_hex(Tn) and is_pen(Tn):
			print(Tn)
			return 

if __name__ == '__main__':
	main()
