# Concealed Square

from itertools import count
from math import sqrt
from itertools import combinations_with_replacement as cwr


template = "1_2_3_4_5_6_7_8_9_0"
def complies(stri2):
	return stri2[::2] == "1234567890"


def main():
	assert complies(template)
	start=int(1929394959697989900**0.5)+7
	adds = [60,40]
	for i in count(0):
		i2 = start**2
		if complies(str(i2)):
			assert int(i2**0.5) == 1389019170
			return
		start -= adds[i%2]

if __name__ == '__main__':
	main()
