#Special Pythagorean Triplet

for c in range(3,998):
	for b in range(2,c):
		for a in range(1,b):
			if a + b + c == 1000 and a**2 + b**2 == c**2:
				print(a*b*c)
