


def comb(val,curri = 0):
	if (val,curri) in d:
		return d[(val,curri)]

	numbers = currencies[curri:]
	if len(numbers) == 1:
		d[(val,curri)] = 1
		return 1
	count = 0
	for i in range(val//numbers[0] + 1):
		if val == i*numbers[0]:
			count += 1
			break
		else:
			count += comb( val - i * numbers[0],curri+1)
	d[(val,curri)] = count
	return count

d = {}
currencies = [200, 100, 50, 20, 10, 5, 2, 1]

assert comb(1) == 1
assert comb(2) == 2
assert comb(3) == 2
assert comb(4) == 3
assert comb(5) == 4
assert comb(200) == 73682, comb(200) 