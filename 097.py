

def main():
	base = 28433
	exp = 7830457
	num_digits = 10
	curr_total = base
	for i in range(exp):
		curr_total = (2 * curr_total) % 10**num_digits
	curr_total+=1
	assert curr_total == 8739992577



if __name__ == '__main__':
	main()