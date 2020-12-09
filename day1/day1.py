path = 'input.txt'

num = []

with open(path) as f:
	for line in f:
		num.append(int(line))

print(num)