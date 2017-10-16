# Double-base palindromes

def is_palindrome(str_num):
	return str_num == str_num[::-1]


def isDoubleBasePalindrome(num):
	return is_palindrome(str(num)) and is_palindrome(bin(num)[2:])

def find_all_double_palindromes_2_n(n):
	dps = set()
	for i in range(n):
		if isDoubleBasePalindrome(i):
			dps.add(i)
	return dps

assert isDoubleBasePalindrome(585)

setdps = find_all_double_palindromes_2_n(1000000)
assert sum(setdps) == 872187