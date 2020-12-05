from math import floor, ceil
f = open("input5.txt", "r")
max=0
for line in f.readlines():
	lrow = 0
	rrow = 127
	lcol = 0
	rcol = 7
	for var in line:
		# print(var)
		if var == 'F':
			rrow = floor((rrow + lrow) / 2)
		if var == 'B':
			lrow = ceil((lrow +rrow) / 2)
		if var == 'R':
			lcol = ceil((lcol +rcol) / 2)
		if var == 'L':
			rcol = floor((lcol +rcol) / 2)
		print(lrow,rrow,lcol,rcol)
	if max < rrow * 8 + rcol:
		max = rrow * 8 + rcol
print(max)
