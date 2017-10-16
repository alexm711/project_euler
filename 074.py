from itertools import combinations_with_replacement as cwr
from itertools import permutations


nr_chain_length = {}

f = [1,1,2,6,24,120,720,5040,40320,362880]

def fact_dig(num):
	return sum(f[int(i)] for i in str(num))

def get_num_leading_ones(numstr):
	for i in range(len(numstr)):
		if numstr[i]!='1':
			return i
	return len(numstr)

def num_permutations(numstr):
	num_set = set()
	for perm in permutations(numstr):
		numstr2 = ''.join(perm)
		if numstr2[0] != '0':
			num_set.add(int(numstr2))
	return len(num_set)

def include_zero_substitutions(numstr):
	num_ones = numstr.count('1')
	options = {numstr}
	for one_count in range(num_ones+1):
		tup = one_count*[0] + (num_ones-one_count)*[1]
		elem = str(numstr)
		for char in tup:
			elem = elem.replace('1',str(char),1)
		options.add(elem)
	return options



def find_nr_chain_length_v2():
	total = 0
	for tup in cwr(range(1,10),6):
		numstr = (''.join([str(i) for i in tup]))
		num_leading_ones = get_num_leading_ones(numstr)
		if num_leading_ones == len(numstr):
			continue
		for i in range(num_leading_ones+1):
			if find_nr_chain_length(int(numstr[i:])) == 60:
				add = 0
				for elem in include_zero_substitutions(numstr[i:]):
					add=num_permutations(elem)
					print(total,add,elem)
					total += add
	return total



def find_nr_chain_length(n,num_leading_zeros=0):
	keys = set()
	total = 0
	new_key = n
	while new_key not in keys:
		keys.add(new_key)
		new_key = fact_dig(new_key)+num_leading_zeros
		total+=1
	return total



def main():
	assert find_nr_chain_length(145) == 1
	assert find_nr_chain_length(540) == 2
	assert find_nr_chain_length(78) == 4
	assert find_nr_chain_length(69) == 5
	assert find_nr_chain_length(872) == 2
	assert find_nr_chain_length(871) == 2
	assert find_nr_chain_length(169) == 3
	total = find_nr_chain_length_v2()
	assert total == 402

if __name__ == '__main__':
	main()