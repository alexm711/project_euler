
# Miller_Rabin primality test from rosetta code
######
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
######

class harshad_helper(object):
	"""docstring for harshad_helper"""
	def __init__(self):
		self.recent_harshads = [1,2,3,4,5,6,7,8,9]
		self.strong_harshads = set()
		self.result = 0
		self.max_digits = 1

	def process_harshad_base(self,base):
		# prime and strong Harshad number of last digit is removed ?
		has_strong_parent = base in self.strong_harshads

		current = base * 10 
		digit_sum = self.digitSum(current)
		for digit in range(10):
			if (current % digit_sum == 0):
				self.recent_harshads.add(current)

				if (is_prime(current // digit_sum)):
					self.strong_harshads.add(current)

			if (has_strong_parent and is_prime(current)):
				self.result+=current
			current+=1
			digit_sum+=1

	def next_round_of_digits(self):
		self.recent_harshads, past_harshads = set(),set(self.recent_harshads)
		for base in past_harshads:
			self.process_harshad_base(base)

	def digitSum(self,num):
		return sum(map(int,str(num)))
 
	def numSRTHarshadPrimes(self,max_digits):
		for numDigits in range(self.max_digits,max_digits):
			self.next_round_of_digits()
		self.max_digits = max(self.max_digits,max_digits)
		return self.result

def main():
	HH = harshad_helper()
	assert HH.numSRTHarshadPrimes(max_digits=4)  == 90619
	assert HH.numSRTHarshadPrimes(max_digits=14) == 696067597313468

if __name__ == '__main__':
	main()