from itertools import count
from itertools import product
from collections import Counter
def P(base,n):
	if base==3:
		return (n*(n+1))//2
	if base == 4:
		return n**2
	if base == 5:
		return (n*(3*n-1))//2
	if base == 6:
		return n*(2*n-1)
	if base == 7:
		return (n*(5*n-3))//2
	if base == 8:
		return n*(3*n-2)

def get_list(base):
	result = []
	for i in count(1):
		temp = P(base,i)
		if temp < 1000:
			continue
		if temp > 9999:
			break
		result.append(temp)
	return result

def isLikelyCyclic(nums):
	strs = [str(num) for num in nums]
	tokens = Counter()
	for num in strs:
		tokens[num[:2]]+=1
		tokens[num[2:]]+=1
	for key in tokens:
		if tokens[key]!=2:
			return False
	return True

def isLikelyCyclicv2(nums):
	token_set = set()
	for num in nums:
		strnum = str(num)
		token_set.update({strnum[:2],strnum[2:]})
	return len(nums)==len(token_set)



def find_set_of_first_n(set_size=3):
	base_lists = []
	for base in range(3,3+set_size):
		base_lists.append(get_list(base))
	# base_sets = []
	# for base_list in base_lists:
	# 	base_sets.append(set(base_list))
	results = []
	for args in product(*base_lists):
		# for j in base_lists[1]:
		# 	for k in base_lists[2]:
		if len(args) > len(set(args)):
			continue
		if  isLikelyCyclicv2(args):
			results.append(args)
				# if stri[:2]==strk[2:] and strj[:2]==stri[2:] and strk[:2]==strj[2:]:
				# 	results.append((i,j,k))
	print(results)


# def find_set_of_first_6(set_size=6):
# 	base_lists = []
# 	for base in range(3,3+set_size):
# 		base_lists.append(get_set(base))
# 	base_sets = []
# 	for base_list in base_lists:
# 		base_sets.append(set(base_list))
# 	results = []
# 	for i in base_lists[0]:
# 		for j in base_lists[1]:
# 			for k in base_lists[2]:
# 				for l in base_lists[3]:
# 					for m in base_lists[4]:
# 						for n in base_lists[5]:
# 							stri = str(i)
# 							strj = str(j)
# 							strk = str(k)

# 							if stri[:2]==strk[2:] and strj[:2]==stri[2:] and strk[:2]==strj[2:]:
# 								results.append((i,j,k))
# 							if stri[:2]==strj[2:] and strk[:2]==stri[2:] and strj[:2]==strk[2:]:
# 								results.append((i,k,j))
# 	print(results)

find_set_of_first_n(3)
find_set_of_first_n(6)



