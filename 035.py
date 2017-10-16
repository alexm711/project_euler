import numpy as np

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


def is_circular(str_prime,primes):
	for i in range(len(str_prime)):
		rot = int(str_prime[i:] + str_prime[:i])
		if rot not in primes:
			return False
	return True


def main():
	primes = set(primesfrom2to(1000000))
	assert is_circular(str(197),primes)

	circular_primes = set(prime for prime in primes if is_circular(str(prime),primes))	
	assert len(circular_primes) == 55

if __name__ == '__main__':
	main()

