count = 0
f = open("input2.txt", "r")
line = f.readline()
while line != "":
	line = line.split()
	low = int(line[0].split('-')[0]) - 1
	high = int(line[0].split('-')[1]) - 1
	letter = line[1].split(':')[0]
	password = line[2]
	num = 0
	if password[low] == letter and password[high] == letter:
		num = 0
	elif password[low] != letter and password[high] != letter:
		num = 0	
	else:
		count += 1
	line = f.readline() 
f.close()
print(count)