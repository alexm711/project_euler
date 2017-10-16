# Passcode derivation
import re
from itertools import count

def find_prefix(attempts):
	prefix = None
	for tup in attempts:
		if not prefix:
			prefix = tup[0]
			continue
		first_num = tup[0]
		if first_num != prefix and prefix in tup:
			prefix = first_num
	for tup in list(attempts):
		if prefix == tup[0]:
			attempts.remove(tup)
			if len(tup)>1:
				attempts.add(tup[1:])
	return str(prefix)

def main():
	with open('079.txt') as f:
		# triangle_data = [list(map(int,i.split())) for i in f.readlines()]
		attempts = [tuple(map(int,[ch for ch in line[:-1]])) for line in f.readlines()]
		attempts = set(attempts)

		guess = ""
		while len(attempts) != 0:
			prefix_num = find_prefix(attempts)
			guess+=prefix_num
		assert guess == "73162890"


if __name__ == '__main__':
	main()
