# Digit fifth powers


def digit_power(num,xth):
	str_num = str(num)
	total = 0
	for ch in str_num:
		total+= int(ch)**xth
	return total == num


def sum_of_xth_pow(xth):
	results = []
	high = (9**xth)*xth
	for num in range(2,high):
		if digit_power(num,xth):
			results.append(num)
	return results



assert sum(sum_of_xth_pow(4)) == 19316, sum_of_xth_pow(4)
assert sum(sum_of_xth_pow(5)) == 443839, sum(sum_of_xth_pow(5))