from fractions import Fraction
from math import ceil

def complies(d):
	fraction_set = set()
	for denom in range(2,d+1):
		for num in range(denom//3+1,ceil(denom/2)):
			frac = Fraction(num,denom)
			# if frac > Fraction(1,3) and frac < 1/2:
			fraction_set.add(frac)

	return len(fraction_set)


### From discussion thread. Much, much faster
def frac(n=12000):
    sieve = [0] * (n + 1)
    for i in range(5, n + 1):
        if i % 3 == 0:
            s_floor = i // 3 + 1
        else:
            s_floor = ceil(i / 3)
        if i % 2 == 0:
            s_ceil = i // 2 - 1
        else:
            s_ceil = i // 2
        s = s_ceil - s_floor + 1
        sieve[i] += s
        for j in range(2 * i, n + 1, i):
            sieve[j] -= sieve[i]
    return sum(sieve)


def main():
	assert complies(d=8)==3
	assert complies(d=12000) == 7295372
	# print(frac())

if __name__ == '__main__':
	main()