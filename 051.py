from importlib import import_module
zero35 = import_module('035')

from itertools import product


class PDRState(object):
	def __init__(self,primes_limit,primes_set,num_members):
		# super(PSetAndList, self).__init__()
		self.primes_limit = primes_limit
		self.primes_set = primes_set
		self.num_members = num_members


	def get_first_prime(self,processed_template):
		template_prime = ''.join(processed_template)
		size_family, first_prime = 0, None
		for digit in range(10):
		
			temp_prime = template_prime.replace('*',str(digit))
			if temp_prime[0] != '0' and int(temp_prime) in self.primes_set:
				size_family+=1
				if not first_prime:
					first_prime = int(temp_prime)

		if size_family >= self.num_members:
			return first_prime
		return self.primes_limit



def make_acceptable_template(template):
	if template[-1] != '*' and  int(template[-1]) % 2 == 0 :
		return 0
	if template.count('0') + template.count('*') == len(template):
		return 0
	if template.count('*') == 0:
		return 0
	for i in range(len(template)):
		if template[i] != 0:
			break
	return template[i:]


def prime_digit_replacement(primes_limit, num_members, max_num_digits):

	primes = set(zero35.primesfrom2to(primes_limit))

	pdr_state = PDRState(primes_limit, primes, num_members)


	first_member = primes_limit
	digit = ['*'] + list(map(str,range(10)))
	for i, template in enumerate(product(digit,repeat=max_num_digits)):
		processed_template = make_acceptable_template(template)
		if not processed_template:
			continue
		first_member = min(first_member,pdr_state.get_first_prime(processed_template))
	assert first_member < primes_limit, "too few primes generated."
	return first_member



def main():
	assert prime_digit_replacement(100,6,2) == 13
	assert prime_digit_replacement(100000,7,5) == 56003
	assert prime_digit_replacement(1000000,8,6) == 121313

if __name__ == '__main__':
	main()
