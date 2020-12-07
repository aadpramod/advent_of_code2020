
f = open("input6.txt", "r")
sum = 0
yes = set()
for line in f.readlines():
	if line == '\n':
		sum += len(yes)
		yes = set()
	else:
		line = line.strip()
		for val in line:
			yes.add(val)
sum += len(yes)
yes = set()

print(sum)
