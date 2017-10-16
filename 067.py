from importlib import import_module
zero18 = import_module('018')
# __import__('018') # for bubble_up

def main():
	with open('067.txt') as f:
		triangle_data = [list(map(int,i.split())) for i in f.readlines()]

	print(zero18.bubble_up(triangle_data))

if __name__ == "__main__":
	main()

