
from itertools import count

def compute(num_digits):
	max_value = 10**num_digits
	strongrepunits = {1}  
	
	for bit_length in range(3, max_value.bit_length() + 1):
		for base in count(2):
			

			value = (base**bit_length - 1) // (base - 1)
			if value >= max_value:
				break
			strongrepunits.add(value)
	
	return strongrepunits

def main():
	assert sum(compute(3)) == 15864
	assert sum(compute(12)) == 336108797689259276


if __name__ == '__main__':
	main()