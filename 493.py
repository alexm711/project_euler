

from math import factorial as f

def prob_particular_color_not_present(n,r,dups):
	result = 1
	for i in range(r):
		result*= (n - dups-i)/(n -i)

	return result


def prob_particular_color_present(n,r,dups):
	return 1-prob_particular_color_not_present(n,r,dups)


def main():
	result = 7 * prob_particular_color_present(70,20,10)
	print(result)
	assert str(result)[:11] == str(6.818741802)

if __name__ == '__main__':
	main()