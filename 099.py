# Largest Exponential
from math import log

def first_is_larger(tup1,tup2):
	#(2**x)**11/x==3**7, where 2**x==3
	if tup1[0] == tup2[0]:
		return tup1[1] > tup2[1]
	x = log(tup2[0],tup1[0])
	new_exp1 = tup1[1] / x
	return new_exp1> tup2[1]

def main():
	with open('099.txt') as f:
		tuples = [tuple(map(int,line.split(','))) for line in f.readlines()]

	assert not first_is_larger((2,11),(3,7))
	assert first_is_larger(tuples[1],tuples[0])
	max_tuple, max_line_num = tuples[0], 1
	for i,tup in enumerate(tuples):
		if first_is_larger(tup,max_tuple):
			max_tuple,max_line_num = tup,i+1
	assert max_line_num== 709

if __name__ == '__main__':
	main()