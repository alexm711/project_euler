# Distinct powers

def distinct_terms(max_term):
	nums = set([a**b for a in range(2,max_term+1) for b in range(2,max_term+1)])
	return sorted(list(nums))

assert len(distinct_terms(5)) == 15, distinct_terms(5)
assert len(distinct_terms(100)) == 9183, len(distinct_terms(100))