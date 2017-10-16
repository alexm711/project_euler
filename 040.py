# Champernowne's constant
from functools import reduce

def prod_of_dns(dns):
	ith, n, digits = 0, 0, []
	curr_dn = dns.pop()
	while True:
		n+=1
		ith += len(str(n))
		str_n = str(n)
		if ith  >= curr_dn:
			next_dig = str_n[curr_dn - ith - 1]
			digits.append(int(next_dig))
			if not dns:
				break
			curr_dn = dns.pop()
	return reduce(lambda x, y: x*y, digits)

assert prod_of_dns([3,2]) == 6
assert prod_of_dns([12]) == 1
assert prod_of_dns([12,10]) == 1, prod_of_dns([12,10])

ds = [1000000, 100000, 10000, 1000, 100,10,1]
assert prod_of_dns(ds) == 210