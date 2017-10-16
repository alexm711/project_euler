from math import sqrt

# prime_array = []
def is_prime(num,prime_array):
	limit = int(sqrt(num)) 
	for x in prime_array:
		if x > limit:
			return True
		if num%x == 0:
			return False

def getnthprime(nth):
	if nth == 1:
		return 2
	prime_array = [2]
	num = 3
	i = 1
	while i < nth:
		if is_prime(num,prime_array):
			i += 1
			prime_array.append(num)
		num+=2
	return num-2

assert getnthprime(2) == 3, getnthprime(2)
assert getnthprime(3) == 5, getnthprime(3)
assert getnthprime(5) == 11, getnthprime(5)
assert getnthprime(6) == 13, getnthprime(6)

n = 10001
print("The {}th prime is: {}".format(n,getnthprime(n)))
