#Square digit chains

from itertools import combinations_with_replacement as cwr
from math import factorial as fact

def digit_sq_sum(n):
	if type(n) is int:
		return sum([int(i) ** 2 for i in str(n)])
	if type(n) is tuple:
		return sum([i**2 for i in n])

def update_set_of_89_chains_to_n_digits(end_in_89,n):
	for i in range(1,n*(9**2)+1):
		temp = i
		while temp not in end_in_89:
			if temp == 1:
				break
			temp = digit_sq_sum(temp)
		else:
			end_in_89.add(i)

def main():
	end_in_89 = {89}
	num_digits = 7
	update_set_of_89_chains_to_n_digits(end_in_89,num_digits)

	factorials = []
	for i in range(0,num_digits+1):
		factorials.append(fact(i))

	count = 0
	for num in cwr(range(10),num_digits):
	    if digit_sq_sum(num) in end_in_89:
	        no_of_permutations = factorials[-1]
	        for digit in range(10):
	            no_of_permutations //= factorials[num.count(digit)]
	        count += no_of_permutations

	print(count)
	assert count == 8581146

if __name__ == '__main__':
	main()