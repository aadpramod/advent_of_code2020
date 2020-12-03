sum = 0
inc = 3
incs = [[1,1],[3,1],[5,1],[7,1], [1,2]]
vals=1

def run_slope(increments):
	column = 0
	count = 0
	rows = 0
	across = increments[0]
	down = increments[1]
	f = open("input3.txt", "r")
	line = f.readline().strip()
	while line != "":
		if rows % down == 0:
			if down == 2:
			if line[column] == '#':
				if down == 2:
				count += 1
			column = (column + across) % len(line)
		line = f.readline().strip()
		rows += 1
	return count

for inc in incs:
	result = run_slope(inc)
	vals *= result
print(vals)


