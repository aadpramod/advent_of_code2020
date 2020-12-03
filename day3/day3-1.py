column = 0
count = 0
sum = 0
f = open("input3.txt", "r")
line = f.readline().strip()
while line != "":
	if line[column] == '#':
		count += 1
	column = (column + 3) % len(line)
	line = f.readline().strip()
	# print(column)
print(count)