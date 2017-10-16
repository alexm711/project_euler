
def word_score(name):
	sub = (ord('A')-1)
	return sum(ch-sub   for ch in name.encode())


def main():
	with open('022.txt') as f:
		names = sorted(f.read().split(','))

	assert word_score("COLIN") == 53
	assert len(names) == 5163, len(names)
	assert names[937].strip("\"") == "COLIN", names[930:940]

	total = 0
	for i, name in enumerate(names,1):
		total+= i * word_score(name.strip("\""))
	assert total == 871198282

if __name__ == '__main__':
	main()