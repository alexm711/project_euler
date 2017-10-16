# Pandigital multiples

from importlib import import_module
zero32 = import_module('032')


def conc_prod_is_pandigital(num):
	conc_prod, base = "", num

	while len(conc_prod) < 9:
		conc_prod += str(base)
		base+=num
	if len(conc_prod) == 9 and zero32.is_pandigital(conc_prod):
		return int(conc_prod)
	return 0

def main():
	assert zero32.is_pandigital(str(192384576))
	assert conc_prod_is_pandigital(192)

	max_pan = max(conc_prod_is_pandigital(i) for i in range(10000))
	assert max_pan == 932718654

if __name__ == '__main__':
	main()

