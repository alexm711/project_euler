# Square root convergents




def main():

	num_instances_of_inequal_digit_length = 0
	num, denom = 3, 2
	
	for i in range(1,1000):
		num, denom = num+2*denom, denom + num
		if len(str(num)) > len(str(denom)):
			num_instances_of_inequal_digit_length+=1

	assert num_instances_of_inequal_digit_length == 153






if __name__ == '__main__':
 	main() 