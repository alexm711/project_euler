
d = {
00 : -3,
1 : 3,
2 : 3,
3 : 5,
4 : 4,
5 : 4,
6 : 3,
7 : 5,
8 : 5,
9 : 4,
10 : 3,
11 : 6,
12 : 6,
13 : 8,
14 : 8,
15 : 7,
16 : 7,
17 : 9,
18 : 8,
19 : 8,
20 : 6,
30 : 6,
40 : 5,
50 : 5,
60 : 5,
70 : 7,
80 : 6,
90 : 6,
"hundred and" : 10,
1000 : 11,
}

def process_numb(i):
	if i in d:
		return d[i]
	total = 0
	stri = str(i)
	assert len(stri) <= 3, "Works only with numbers sub 1000"
	# lowest 2
	low2 = stri[-2:]
	if int(low2) in d:
		total+=d[int(low2)]
	else:
		total+= d[int(low2[0])*10] + d[int(low2[1])]

	if len(stri) > 2:
		total+= d["hundred and"] + d[int(stri[-3])]
	return total


def written_out(iterator):
	total = 0
	for i in iterator:
		total+= process_numb(i)
	return total
	
assert process_numb(1000) == 11
assert process_numb(342) == 23
assert process_numb(115) == 20
assert written_out(range(1,6)) == 19
print(written_out(range(1,1001)))