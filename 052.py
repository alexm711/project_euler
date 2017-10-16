# Permuted multiples

import itertools


def same_digits(int1,int2):
	return sorted(str(int1)) == sorted(str(int2))

def main():
	assert same_digits(125874,2*125874)
	# return 2
	for n in itertools.count(2):
		for i in range(2,7):
			if not same_digits(n,i*n):
				break
		else:
			print(n)
			assert n == 142857
			return 






if __name__ == '__main__':
	main()