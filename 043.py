from itertools import permutations

divisors = [2,3,5,7,11,13,17]

# ss_div is sub_string_divisibility
def ss_div(n):
	for i in range(1,8):
		sub_string = int(n[i:i+3])
		if sub_string % divisors[i-1] != 0:
			return False
	return int(n)

def main():
	assert ss_div(str(1406357289))
	assert not ss_div(str(4103657289))

	total = sum(ss_div(''.join(p)) for p in permutations('0123456789'))
	assert total == 16695334890


if __name__ == '__main__':
	main()