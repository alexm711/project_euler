
import numpy as np
import heapq

def compress_matrix(npmatrix):
	# print(npmatrix.shape)
	max_idx = len(npmatrix)-1
	visited, q = set(), [(npmatrix[0,0],0,0)]
	while q:
		score,row,col = heapq.heappop(q)
		if (row,col) in visited:
			continue
		visited.add((row,col))

		if row==col==max_idx:
			return score
		if row < max_idx:
			heapq.heappush(q, (score+npmatrix[row+1,col],row+1,col))
		if col < max_idx:
			heapq.heappush(q, (score+npmatrix[row,col+1],row,col+1))

	return npmatrix[0,0]

test = np.matrix([
	[131,201,630,537,805],
	[673,96,803,699,732],
	[234,342,746,497,524],
	[103,965,422,121,37],
	[18,150,111,956,331]])

def main():
	with open('081.txt') as f:
		matrix = np.matrix([list(map(int,line.split(','))) for line in f.readlines()])

	assert compress_matrix(test) == 2427
	assert compress_matrix(matrix) == 427337

if __name__ == '__main__':
	main()