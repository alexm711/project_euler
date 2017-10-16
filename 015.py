from math import factorial

def num_paths(n):
	perms = factorial(2*n)
	return perms/(factorial(n)**2)

assert num_paths(2) == 6, num_paths(2)
print(num_paths(20))
