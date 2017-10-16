# Powerful digit sum

from itertools import product

def main():
	max_sum = 0
	for a,b in product(range(100),range(100)):
		max_sum = max(max_sum,   sum(int(char) for char in str(a**b))  )

	assert max_sum == 972

if __name__ == '__main__':
	main()