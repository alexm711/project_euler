def M(p,q,N):



M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100 that is divisible by both 2 and 73.

Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.


def main():
	assert M(2,3,100) == 96
	assert M(3,5,100) == 75
	assert M(2,73,100) == 0
	assert S(10**2) == 2262
	print(S(10**7))

if __name__ == '__main__':
	main()