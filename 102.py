# Triangle containment

def contains_origin(tup):
	coords = sorted([tup[i*2:i*2+2] for i in range(3)], key=lambda coord: coord[1])
	if coords[0][1]>0 or coords[2][1]<0:
		return False
	slope_1_to_3 = (coords[2][0]-coords[0][0]) / (coords[2][1]-coords[0][1])
	at_zero_1 = -coords[0][1]*slope_1_to_3 + coords[0][0]
	
	if coords[1][1] < 0:
		slope_2 = (coords[2][0]-coords[1][0]) / (coords[2][1]-coords[1][1])
	else:
		slope_2 = (coords[0][0]-coords[1][0]) / (coords[0][1]-coords[1][1])
	at_zero_2 = -coords[1][1]*slope_2 + coords[1][0]

	return abs(at_zero_1-at_zero_2) > abs(at_zero_1+at_zero_2)



def main():
	with open('102.txt') as f:
		tuples = [tuple(map(int,line.split(','))) for line in f.readlines()]
	assert contains_origin(tuples[0])
	assert not contains_origin(tuples[1])
	tot = sum([contains_origin(tup) for tup in tuples])
	assert tot == 228

if __name__ == '__main__':
	main()