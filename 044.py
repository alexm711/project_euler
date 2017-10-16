# Pentagon numbers
from math import sqrt
import itertools


class PnState(object):
	def __init__(self):
		# super(PSetAndList, self).__init__()
		self.Pn_set = set()
		self.Pn_list = [0]

	def gen_next(self):
		nxt = len(self.Pn_list)
		term = nxt*(3*nxt-1)//2
		self.Pn_list.append(term)
		self.Pn_set.add(term)

	def Pn(self,n):
		while len(self.Pn_list) <= n:
			self.gen_next()
		return self.Pn_list[n]


	def is_Pn(self,Pn):
		# n = (sqrt(24*Pn+1)+1)/6
		while self.Pn_list[-1] < Pn:
			self.gen_next()
		return Pn in self.Pn_set
				

def main():
	min_d = 0
	Pn_state = PnState()

	for a in itertools.count(2):
		Pa = Pn_state.Pn(a)
		if min_d and Pa - Pn_state.Pn(a-1) >= min_d:
			break
		for b in range(a-1,0,-1):
			Pb = Pn_state.Pn(b)
			diff = Pa - Pb
			if min_d and diff >= min_d:
				break
			elif Pn_state.is_Pn(Pa+Pb) and Pn_state.is_Pn(diff):
				min_d = diff

	print(min_d)
	assert min_d == 5482660


if __name__ == '__main__':
	main()
