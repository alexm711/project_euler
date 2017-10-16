
def bubble_up(triangle_data):
	last_row = triangle_data[-1]
	for row in triangle_data[-2::-1]:
		new_row = []
		for i,col in enumerate(row):
			new_row.append(col + max(last_row[i],last_row[i+1]) )
		last_row = new_row
	return last_row[0]



def main():
	with open('018.txt') as f:
		triangle_data = [list(map(int,i.split())) for i in f.readlines()]

	test = [
	[3],
	[7, 4],
	[2, 4, 6],
	[8, 5, 9, 3]]

	assert bubble_up(test) == 23,  bubble_up(test)
	print(bubble_up(triangle_data))

if __name__ == "__main__":
	main()

