

def main():

	num = str(sum(i**i for i in range(1,1001)))
	# print(num[-10:])
	assert num[-10:] == "9110846700"


if __name__ == '__main__':
	main()