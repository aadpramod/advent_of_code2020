count = 0
f = open("input2.txt", "r")
line = f.readline()
while line != "":
	line = line.split()
	low = int(line[0].split('-')[0])
	high = int(line[0].split('-')[1])
	letter = line[1].split(':')[0]
	password = line[2]
	num = 0
	for val in password:
		if val == letter:
			num += 1
	print(num, high, low)
	if num <= high and num >= low:
		count += 1
	line = f.readline() 
f.close()
print(count)