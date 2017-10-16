

with open('013.txt') as f:
    Sum = sum([int(i) for i in f.readlines()])

print(str(Sum)[:10])
