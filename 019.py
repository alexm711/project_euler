from datetime import datetime as dt

count = 0
for y in range(1901,2001):
	for m in range(1,13):
		date = dt(y,m,1)
		if dt.strftime(date,'%A') == 'Sunday':
			count+=1
print(count)
