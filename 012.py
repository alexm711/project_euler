
from math import sqrt

def get_num_divisors(n):
    num_div = 0
    upper = int(sqrt(n)) 
    for i in range(1 , upper +1):
        if n % i == 0:
            num_div += 2
            
    if upper ** 2 == n :
        num_div -= 1 
    return num_div


def search_for_triangle_number(num_divisors, initial_lower_guess_idx=2):
	triangle_number = sum(range(initial_lower_guess_idx))
	i = initial_lower_guess_idx
	while True:
		triangle_number+=i
		if num_divisors < get_num_divisors(triangle_number):
			return triangle_number
		i+=1
	return triangle_number


assert search_for_triangle_number(5,5) == 28,  search_for_triangle_number(5,5)
print(search_for_triangle_number(500,12000))
