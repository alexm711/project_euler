# Prime pair sets

from importlib import import_module
from itertools import product
zero35 = import_module('035')
zero387 = import_module('387')
import networkx as nx


def attempt():
	G=nx.Graph()
	max_prime = 700
	primes = zero35.primesfrom2to(max_prime)
	primes_set = set(primes)
	G.add_nodes_from(primes)
	for prime1, prime2 in product(primes,primes):
		if prime1 == prime2:
			continue
		concat1, concat2 = int(str(prime1)+str(prime2)), int(str(prime2)+str(prime1))
		if zero387.is_prime(concat1) and zero387.is_prime(concat2):
		# if int(concat1) in primes_set and int(concat2) in primes_set:
			G.add_edge(prime1,prime2)
	temp = nx.connected_components(G)
	# print(len(temp))
	for resp in nx.connected_components(G):
		if len(resp) >= 4:
			print(resp)


def find_prime_pair_set(max_prime,num_primes):
	primes = zero35.primesfrom2to(max_prime)
	primes_set = zero35.primesfrom2to(max_prime)
	prime_pairs = set()
	for prime1, prime2 in product(primes,primes):
		if prime1 == prime2:
			continue
		concat1, concat2 = str(prime1)+str(prime2), str(prime2)+str(prime1)
		if int(concat1) in primes_set and int(concat2) in primes_set:
			prime_pairs.add( tuple(sorted(prime1,prime2))   ) 



# def main():
# 	# attempt()
# 	# assert find_prime_pair_set(max_prime=700000,num_primes=4) == 792
# 	# print find_prime_pair_set(max_prime=10000000,num_primes=4)



# if __name__ == '__main__':
# 	main()

G=nx.Graph()
max_prime = 700
primes = zero35.primesfrom2to(max_prime)
primes_set = set(primes)
G.add_nodes_from(primes)
for prime1, prime2 in product(primes,primes):
	if prime1 == prime2:
		continue
	concat1, concat2 = int(str(prime1)+str(prime2)), int(str(prime2)+str(prime1))
	if zero387.is_prime(concat1) and zero387.is_prime(concat2):
	# if int(concat1) in primes_set and int(concat2) in primes_set:
		G.add_edge(prime1,prime2)
temp = nx.connected_components(G)
# print(len(temp))

# for resp in nx.connected_components(G):
# 	if len(resp) >= 4:
# 		print(resp)



import networkx as nx
from networkx.algorithms.approximation import ramsey


def max_clique(G):
    if G is None:
        raise ValueError("Expected NetworkX graph!")

    # finding the maximum clique in a graph is equivalent to finding
    # the independent set in the complementary graph
    cgraph = nx.complement(G)
    iset, _ = clique_removal(cgraph)
    return iset

def clique_removal(G):
    graph = G.copy()
    c_i, i_i = ramsey.ramsey_R2(graph)
    cliques = [c_i]
    isets = [i_i]
    while graph:
        graph.remove_nodes_from(c_i)
        c_i, i_i = ramsey.ramsey_R2(graph)
        if c_i:
            cliques.append(c_i)
        if i_i:
            isets.append(i_i)

    maxiset = max(isets)
    return maxiset, cliques

