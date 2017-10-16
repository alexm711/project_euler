from math import sqrt

def compute():
	return sum(i for i in range(1, 10000) if has_pandigital_product(i))

d = {
1: "1",
2: "12",
3: "123",
4: "1234",
5: "12345",
6: "123456",
7: "1234567",
8: "12345678",
9: "123456789"
}

def is_pandigital(int_str):
	return "".join(sorted(int_str)) == d[len(int_str)]

def has_pandigital_product(n):
	for i in range(1, int(sqrt(n)) + 1):
		int_str = "{}{}{}".format(n,i,n//i)
		if n % i == 0 and len(int_str)==9 and is_pandigital(int_str):
			return True
	return False



def main():
	assert compute() == 45228

if __name__ == '__main__':
	main()