
def sum_diag_spiral(size):
	total = 1
	for i in range(1,size//2+1):
		multiple = (i*2+1)**2
		last_multiple = (i*2-1)**2
		diags = (i for i in range(last_multiple+2*i,multiple+1,2*i) )
		# print(diags)
		total+=sum(diags)
	return total

assert sum_diag_spiral(3) == 25, sum_diag_spiral(3)
assert sum_diag_spiral(5) == 101, sum_diag_spiral(5)
assert sum_diag_spiral(1001) == 669171001, sum_diag_spiral(1001)
