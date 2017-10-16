# Reciprocal cycles

def iter_div(r,n):
	return r/n, (r%n)*10


def denom_length_recurring_cycle(n):
	past_fracs = set()
	has_cycle=False
	remainder = 1
	while remainder != 0:
		frac, remainder = iter_div(remainder,n)
		if frac in past_fracs:
			has_cycle = True
			break
		past_fracs.add(frac)
	if has_cycle:
		curr_frac = remainder/n
		iters = 0
		while frac != curr_frac:

			curr_frac, remainder = iter_div(remainder,n)
			iters += 1
		return iters
	return 0

def find_longest_cycle(n):
	assert n>=2
	longest, max_d = 0,2
	for d in range(2,n+1):
		if denom_length_recurring_cycle(d) > longest:
			longest = denom_length_recurring_cycle(d)
			max_d = d
	return(max_d)

assert denom_length_recurring_cycle(7) == 6, denom_length_recurring_cycle(7)
assert find_longest_cycle(7) == 7, find_longest_cycle(7)
assert find_longest_cycle(10) == 7, find_longest_cycle(10)
assert find_longest_cycle(1000) == 983, find_longest_cycle(1000)
		
