from fractions import Fraction

def getp_v(nth):
	if (nth+2)%3==0:
		return 2*(nth+2)//3
	return 1
	if nth%2!=0:
		return 1
	return nth//2


def e(nth):
	frac = Fraction(0,1)
	for ith in range(nth-1,-1,-1):
		frac = Fraction(1,(getp_v(ith)+frac))
	return 2 + frac



def main():
	assert sum(map(int,str(e(9).numerator))) == 17
	assert sum(map(int,str(e(99).numerator))) == 272

if __name__ == '__main__':
	main()