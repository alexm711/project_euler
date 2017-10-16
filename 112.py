# Bouncy numbers
from itertools import count


def increasing(digit_tup):
	for i in range(1,len(digit_tup)):
		if digit_tup[i]<digit_tup[i-1]:
			return False
	return True

def decreasing(digit_tup):
	for i in range(1,len(digit_tup)):
		if digit_tup[i]>digit_tup[i-1]:
			return False
	return True

def bouncy(num):
	digit_tup = tuple(map(int,str(num)))
	return not increasing(digit_tup) and not decreasing(digit_tup)
		

def percentage_bouncy_numbers(perc):
	total_bouncies = 0
	for num in count(1):
		if bouncy(num):
			total_bouncies+=1
		if total_bouncies >= perc * num:
			return num

def main():
	assert percentage_bouncy_numbers(0.5) == 538
	assert percentage_bouncy_numbers(0.9) == 21780
	assert percentage_bouncy_numbers(0.99) == 1587000


if __name__ == '__main__':
	main()