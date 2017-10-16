from math import sqrt
from itertools import count

def getPeriod(N,prec=8):
	a_0 = sqrt(N)
	if a_0%1==0:
		return 0
	a_0 = int(a_0)
	states = [(a_0,0,1)]
	for i in count(1):
		a,m,d = states[-1]
		m_ = d*a-m
		d_ = (N - m_**2)// d
		a_ = (a_0+m_)//d_
		new_state = (a_,m_,d_)
		if new_state in states:
			return len(states)-1
		states.append((a_,m_,d_))

odds = 0
for i in range(2,10001):
	if getPeriod(i)%2!=0:
		odds+=1
print(odds)
