import numpy as np

def prod(int_string_array):
	result = 1
	for int_string in int_string_array:
		result*=int(int_string)
	return result


def max_prod_grid(grid_data,num_adj):
	max_prod = 0
	cols, rows = len(grid_data[0]), len(grid_data)

	# Vertical
	for col in range(cols):
		for row in range(rows-num_adj+1):
			max_prod = max(max_prod,prod(grid_data[row:row+num_adj,col] ))

	# Horizontal
	for row in range(rows):
		for col in range(cols-num_adj+1):
			max_prod = max(max_prod,prod(grid_data[row,col:col+num_adj] ))

	# Diagonal
	for col in range(cols-num_adj+1):
		for row in range(rows-num_adj+1):
			grid_subset = grid_data[row:row+num_adj,col:col+num_adj]
			max_prod = max(max_prod,prod(grid_subset.diagonal()), prod(np.fliplr(grid_subset).diagonal()))

	return max_prod


with open('011.txt') as f:
    grid_data = [i.split() for i in f.readlines()]

grid_data = np.array(grid_data)

print(max_prod_grid(grid_data,4) )