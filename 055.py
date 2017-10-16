# Lychrel numbers

from importlib import import_module
zerozero4 = import_module('004')

def is_lychrel(n):
	curr_n = n
	for i in range(50):
		curr_n+=  int(str(curr_n)[::-1])
		if zerozero4.is_palindrome(curr_n):
			return False
	return True

def main():

	assert not is_lychrel(47)
	assert is_lychrel(196)
	assert sum(is_lychrel(n) for n in range(1,10000)) == 249


if __name__ == '__main__':
	main()