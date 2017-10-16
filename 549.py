# Divisibility of factorials


from itertools import count

# def get_divisors(n):
# 	divisors = [1,n]
# 	low = 2
# 	while low<=int(n**0.5):
# 		if n%low==0:
# 			divisors.extend([low,n//low])
# 		low+=1
# 	return divisors
def get_prime_factors(num,get_largest=False):
	if num not in pf_dict or get_largest:
		n = num
		prime_factors = []
		i = 2
		while i * i <= n and n not in pf_dict:
			while n % i == 0:
				n = n // i
				prime_factors.append(i)
			i = i + 1
		if n in pf_dict:
			prime_factors = sorted(prime_factors+pf_dict[n])
		elif n != 1:
			prime_factors.append(int(n))
		if get_largest:
			return prime_factors[-1]
		pf_dict[num] = prime_factors
		# return prime_factors
	return pf_dict[num]

# print (n)

def remove_prime_factors_up_to(largest_factor,n):
	curr_len = len(pf_up_to)
	while curr_len + 1 < largest_factor:
		new_dict = {}

		next_get = get_prime_factors(curr_len+2)
		prev_dict = pf_up_to[-1]
		keys = set(next_get + list(prev_dict.keys()))


		for key in keys:
			new_dict[key] = prev_dict.get(key,0)+next_get.count(key)

		pf_up_to.append(new_dict)
		curr_len+=1
	relevant_dict = pf_up_to[largest_factor-2]
	for key, dups in relevant_dict.items():
		for i in range(dups):
			if n%key==0:
				n//=key
			else:
				break
	# print(curr,pf_up_to)
	return n



def s(n):
	# print("working with,", n)
	# curr = n
	largest_factor = get_prime_factors(n,get_largest=True)
	curr = remove_prime_factors_up_to(largest_factor,n)
	if curr == 1:
		return largest_factor
	for m in count(largest_factor+1):
		assert m <= n
		m_prime_factors = get_prime_factors(m)
		for pf in m_prime_factors:
			if curr%pf==0:
				curr//=pf
				if curr == 1:
					return m
		# print(m,curr)
	# return m	
def S(n):
	return sum(s(i) for i in range(2,n+1))

pf_dict = {}
pf_up_to = [{2:1}]

def main():
	assert s(10) == 5, s(10)
	assert s(25) == 10, s(25)
	assert S(100) == 2012, S(100)
	# print(pf_up_to)
	# print(S(10**8))
	assert S(10**8) == 476001479068717

if __name__ == '__main__':
	main()



