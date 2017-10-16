# Prime generating integers

from importlib import import_module
zero35 = import_module('035')

# def get_divisors(n):
# 	divisors = {1,n}
# 	low = 2
# 	while low<=int(n**0.5):
# 		if n%low==0:
# 			divisors.update({low,n//low})
# 		low+=1
# 	return divisors

def complies(n,primes_set):
	# divisors = {1,n}
	if n + 1 not in primes_set or 2 + n/2 not in primes_set:
		return False
	low = 3
	while low<=int(n**0.5)+1:
		if n%low==0 and (low + n//low not in primes_set):
			return False
		low+=1
	return True




# def complies(n,primes_set):
# 	for d in get_divisors(n):
# 		# print(d)
# 		if d + n/d not in primes_set:
# 			return False
# 	return True



def main():
	primes_limit = 10**8
	primes = zero35.primesfrom2to(primes_limit)
	primes_set = set(primes)
	count = 1
	assert complies(30,primes_set)
	for n in primes:
		if complies(n-1,primes_set):
			count+=(n-1)

	print(count)
	assert count == 1739023853137



if __name__ == '__main__':
	main()