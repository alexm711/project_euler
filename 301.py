# 


# def X(n1,n2,n3):
# 	return n1 ^ n2 ^ n3

# def Xdup(n):
# 	result = n ^ (n*2) ^ (n*3)
# 	print(n,result, bin(n)[2:],bin(2*n)[2:],bin(3*n)[2:],"\n")
# 	return result


def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
	return a
print fib(5)

def main():
	total = 0
	for n in range(1,1+2**30):
		total+= n ^ (n*2) ^ (n*3) ==  0
	print(total)
	assert total == 2178309 == fib(32)
	# assert 


if __name__ == '__main__':
	main()



