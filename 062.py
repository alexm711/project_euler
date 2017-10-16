# Cubic permutations
from itertools import combinations_with_replacement as cwr
from itertools import count, permutations


def up2npermutations(n):
	d = {}
	for i in count(2):
		num = i**3
		result = ''.join(sorted(str(num)))
		d[result] = d.get(result,[]) + [num]
		if len(d[result]) == n:
			return d[result]

def main():
	assert up2npermutations(3)[0] == 41063625
	assert up2npermutations(5)[0] == 127035954683

if __name__ == '__main__':
	main()