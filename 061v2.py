# https://blog.dreamshire.com/project-euler-61-solution/
from collections import defaultdict

def fn(n):
    return (3,n*(n+1)/2), (4,n*n), (5,n*(3*n-1)/2), (6,n*(2*n-1)), (7,n*(5*n-3)/2), (8,n*(3*n-2))
 
def next(types, data):
    if len(types) == 6 and data[0] // 100 == data[-1] % 100:
        print(data, sum(data))
    else:
        for t, n in ds.get((types[-1], data[-1]), []):
            if t not in types:
                next(types+[t], data+[n])
 
p = []          # build a list of polygonal numbers with their type (type, pnum)

for n in range(19,141):  # 1st octogonal number > 999 & last triangle number < 10000
    for cycle_type, data in fn(n):
        if 1000 <= data <= 9999 and data % 100 > 9:
            p.append( (cycle_type, data) ) 
 
ds = defaultdict(list)         # build a dictionary of tuples
for t1, d1 in p:
    for t2, d2 in p:
        if t1 != t2 and d1 % 100 == d2 // 100:
            ds[t1, d1].append((t2, d2))
 
print("Project Euler 61 Solution Set")
for cycle_type, data in ds:
    next([cycle_type], [data])