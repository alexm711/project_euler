# Counting rectangles

def num_rectangles(H,W):
	total = 0
	for h in range(1,H+1):
		for w in range(1,W+1):
			total+= (H-h+1)*(W-w+1)
	return total


def main():
	target = 2000000
	best_tup = (1,2000)
	H,W = best_tup
	bestdiff = num_rectangles(H,W)-target
	while W > H:
		H+=1
		past_num, next_num = num_rectangles(H,W), num_rectangles(H,W)
		while next_num> target:
			W-=1
			past_num,next_num = next_num,num_rectangles(H,W)
		curr_diff = min(target-next_num,past_num-target)
		if curr_diff < bestdiff:
			bestdiff,best_tup = curr_diff,(W,H)

	assert best_tup[0]*best_tup[1]==2772

if __name__ == '__main__':
	main()

