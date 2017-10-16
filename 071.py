# ordered fractions

from decimal import *

def find_left_neighbor(n,d):
	curr_max, curr_num = 0 , None
	for denom in range(3,d+1):
		num = (n * denom)//1 
		while num / denom >= n:
			num-=1
		if num / denom > curr_max:
			curr_max, curr_num = num / denom  , num
	return int(curr_num)



def main():
	assert find_left_neighbor(Decimal(3)/7,d = 8) == 2, find_left_neighbor(Decimal(3)/7,d = 8)
	assert find_left_neighbor(Decimal(3)/7,d = 1000000) == 428570





if __name__ == '__main__':
	main()