


from math import factorial

def get_nth_lexi_permutation(num_digits,nth):
	digits = list(range(num_digits))
	answer_list = []
	current_toll = 0
	for idx in range(len(digits)):
		multiple = factorial(num_digits-idx-1)
		for i in reversed(range(len(digits))):
			if i*multiple + current_toll < nth:
				answer_list.append(digits[i])
				del digits[i]
				current_toll+=i*multiple
				break
	return ''.join(map(str,answer_list))


test_answers = ["012", "021", "102", "120", "201", "210"]
for i in range(factorial(3)):
	assert get_nth_lexi_permutation(3,i+1) == test_answers[i]
assert get_nth_lexi_permutation(10,1000000) == str(2783915460)
print(get_nth_lexi_permutation(10,1000000))