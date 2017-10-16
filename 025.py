
fib_tup =  (144,89)
idx = 12
limit = 10**999
while fib_tup[0]< limit:
	fib_tup = (fib_tup[0]+fib_tup[1],fib_tup[0])
	idx+=1
print(idx)