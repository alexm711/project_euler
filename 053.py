# Combinatoric selections


from math import factorial as f

def nCr(n,r):
    return f(n) // f(r) // f(n-r)


def main():
	assert nCr(5,3) == 10
	assert nCr(23,10) == 1144066
	num_values = 0

	for n in range(1,101):
		for r in range(1,n//2+1):
			if nCr(n,r)> 10**6:
				num_values+=2*(n//2+1 -r) - (1 if n%2 == 0 else 0)
				break



	assert num_values == 4075, num_values		



if __name__ == '__main__':
	main()