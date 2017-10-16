def is_palindrome(num):
	strnum = str(num)
	return strnum == strnum[::-1]

def main():
	maxnum, lowbound = 1, 0
	for high in range(999,1,-1):
		for low in range(high,lowbound,-1):
			if is_palindrome(high*low) and high*low > maxnum:
				maxnum = high*low
				lowbound = low
				break
	print(maxnum)


if __name__ == '__main__':
	main()


