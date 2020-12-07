
f = open("input6.txt", "r")
sum = 0
yes = {}
count = 0
for line in f.readlines():
	if line == '\n':
		for key in yes:
			if yes[key] == count:
				sum += 1
		count = 0
		yes = {}
	else:
		count += 1
		line = line.strip()
		for val in line:
			if val in yes:
				yes[val] += 1
			else: yes[val] = 1
for key in yes:
			if yes[key] == count:
				sum += 1

print(sum)
