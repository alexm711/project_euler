# Dice Game
from math import factorial as f
from itertools import combinations_with_replacement as cwr


f = [1,1,2,6,24,120,720,5040,40320,362880]
def num_perms(combo):
	combo_str = ''.join(map(str,combo))
	total = f[len(combo_str)]
	for dig in range(1,7):
		total/=f[combo_str.count(str(dig))]
	return total



def main():
	colin_probs = [0]*(36-6+1)
	peter_probs = [0]*(36-9+1)

	for combo in cwr(range(1,7),6):
		score = sum(combo)
		colin_probs[score-6] +=num_perms(combo)

	for combo in cwr(range(1,5),9):
		score = sum(combo)
		peter_probs[score-9]+=num_perms(combo)

	colin_denom = sum(colin_probs)
	peter_denom = sum(peter_probs)
	result = 0
	for pete_score,pp in enumerate(peter_probs,9):
		result+=(pp)*(sum(colin_probs[0:pete_score-6]))
		
	print(result/(colin_denom*peter_denom))

if __name__ == '__main__':
	main()