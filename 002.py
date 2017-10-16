first, second = 1, 2
curr_sum = 2
while second< 4000000:
	temp = first+second
	first = second
	second = temp
	if second % 2 == 0:
		curr_sum+=second
print(curr_sum)
