
from itertools import count

def search_for_nth_powers():
	# ansatz, bases >= 10 will not produce n powers of length n9
	counter = 0 # base case base =1, works for n = 1 
	for base in range(1,10):
		for exp in count(1):
			cand = base**exp
			if exp == len(str(cand)):
				counter+=1
			if len(str(cand)) < exp:
				break
	return counter

def main():
	print(search_for_nth_powers())
	assert search_for_nth_powers() == 49

if __name__ == '__main__':
	main()