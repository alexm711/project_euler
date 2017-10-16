# Digit Canceling Fractions
from itertools import product

def digit_canceling(frac,num,denom,i,j):
	return denom[j] != '0' and frac == int(num[i])/int(denom[j]) and \
	 			num[(i+1)%2]==denom[(j+1)%2] and  num[(i+1)%2]!='0'

def is_digit_canceling_fraction(a,b):
	frac = a/b
	for i,j in product(range(2),range(2)):
		if digit_canceling(frac,str(a),str(b),i,j):
			return True
	return False 



def iterate_over_two_by_two_digit_fractions():
	results = [] 
	for denom in range(10,100):
		for num in range(10,denom):
			if num!=denom and is_digit_canceling_fraction(num,denom):
				results.append((num,denom))
	return results

def main():
	assert is_digit_canceling_fraction(49,98) 

	fracs_list = iterate_over_two_by_two_digit_fractions()
	assert len(fracs_list) == 4
	print(fracs_list)
	
if __name__ == '__main__':
	main()


