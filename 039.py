# Integer right triangles

def is_right_tri(a,b,c):
	return a**2 + b**2 == c**2

def num_right_tri_solutions(p):
	sols = set()
	for c in range(p//3,p-1):
		for b in range(min(c,p-c)//2,min(c,p-c)):
			a = p-c-b
			if a<=b and is_right_tri(a,b,c):
				sols.add((a,b,c))
	return sols

assert num_right_tri_solutions(120) == {(20,48,52), (24,45,51), (30,40,50)}, num_right_tri_solutions(120)

def get_max_p(n): 
	max_p,max_length = 0,0
	for p in range(n):
		sets = num_right_tri_solutions(p)
		if max_length<len(sets):
			max_p = p
			max_length = len(sets)
	return max_p
	
max_p = get_max_p(1000)
assert max_p == 840