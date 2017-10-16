# Counting summations

def num_sum(num,max_n):
	if num<=0:
		return 0
	if num==1 or max_n == 1:
		return 1
	if (num,max_n) not in diction:
		total = 1 if max_n >= num else 0 
		for next_num in range(max_n,0,-1):
			total+=num_sum(num-next_num,next_num)
		diction[(num,max_n)] = total
	return diction[(num,max_n)]


diction = {(2,2):2,(3,3):3,(3,2):2}

def main():

	assert num_sum(5,5)-1 == 6
	assert num_sum(6,6)-1 == 10
	assert num_sum(100,100)-1 == 190569291


if __name__ == '__main__':
	main()