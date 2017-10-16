
def seq(n):
	if n%2==0:
		return n//2
	return (3*n)+1

def getLength(i,trace=False):
	curr = i
	iters = 0
	elems = []
	while curr not in d:
		elems.append(curr)
		curr = seq(curr)
		iters+=1
	if trace:
		print(elems,curr)
	for idx, elem in enumerate(elems[::-1],1):
		d[elem] = idx + d[curr]
	return d[i]

d = {1 : 1}

max_length,max_num = 0, 0
for idx in range(1,1000001):
	if idx not in d:
		if max_length < getLength(idx):
			max_length = getLength(idx)
			max_num = idx
print("max_length: {} at number: {}".format(max_length,max_num) )