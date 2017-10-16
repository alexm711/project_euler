
from importlib import import_module
from itertools import product
zero35 = import_module('035')
primes = zero35.primesfrom2to(5000)


def isPerm(a,b):
    return sorted(str(a)) == sorted(str(b))

best = 1
limit = 10**7
bestRatio = limit
 
for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        n = primes[i] * primes[j]
        if n> limit:
            break
        phi = (primes[i] - 1) * (primes[j] - 1)
        ratio = n / phi
 
        if (isPerm(n, phi) and bestRatio > ratio):
            best = n
            bestRatio = ratio
print(best)
   