
import numpy as np


test1 = np.matrix([
[  7,  53, 183, 439, 863],
[497, 383, 563,  79, 973],
[287,  63, 343, 169, 583],
[627, 343, 773, 959, 943],
[767, 473, 103, 699, 303]])

test2 = np.matrix([
[  7,  53, 183, 439, 863, 497, 383, 563,  79, 973, 287,  63, 343, 169, 583],
[627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
[447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
[217, 623,   3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350],
[960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
[870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803],
[973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
[322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973],
[445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848],
[414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
[184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
[821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574],
[ 34, 124,   4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
[815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
[813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805]])

def get_subset(matrix):
	dup_cols = []
	dup_rows = set()
	n = matrix.shape[0]

	for col in range(n):
		if list(matrix[:,col]).count(0.) > 1:
			for row in range(n):
				if matrix[row,col] == 0.:
					dup_rows.add(row)
		else:
			dup_cols.append(col)
	new_mat = np.ones((len(dup_rows),len(dup_cols)))
	for r,row in enumerate(sorted(dup_rows)):
		for c,col in enumerate(dup_cols):
			new_mat[r,c] = matrix[row,col]
	return new_mat, set(dup_rows), set(dup_cols)



		# inv_mat[:,col] -= inv_mat[:,col].min() * np.ones((n,1))
	print(inv_mat)

def cantAssign(matrix):
	print("checking if can assign\n\n")
	print(matrix,"\n\n")

	n = matrix.shape[0]
	cols = set()
	for r,row in enumerate(matrix):
		for c in range(n):
			if row.item(c) == 0.:
				print(cols,c)
				if c in cols:
					return True
				cols.add(c)
	return len(cols) != n




def hungarian(matrix):
	print(matrix)
	inv_mat = matrix.max()*np.ones(matrix.shape) - matrix
	#step 1
	print(inv_mat)

	n = matrix.shape[0]
	for row in range(n):
		inv_mat[row] -= inv_mat[row].min() * np.ones(n)
	print(inv_mat)

	for col in range(n):
		inv_mat[:,col] -= inv_mat[:,col].min() * np.ones((n,1))
	# step 3-4
	while cantAssign(inv_mat):
		new_matrix, dup_rows, dup_cols = get_subset(inv_mat)
		# print(new_matrix)
		# print(new_matrix.min())
		remainder_min = new_matrix.min()
		for row in range(n):
			for col in range(n):
				if row in dup_rows and col in dup_cols:
					inv_mat[row,col]-=remainder_min
				else:
					inv_mat[row,col]+=remainder_min
	print("tada")




from scipy.optimize import linear_sum_assignment

row_ind, col_ind = linear_sum_assignment(-test1)
assert test1[row_ind, col_ind].sum() == 3315

row_ind, col_ind = linear_sum_assignment(-test2)
assert test2[row_ind, col_ind].sum() == 13938
