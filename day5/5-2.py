from math import floor, ceil
f = open("input5.txt", "r")
loc = {}
for i in range(0,817):
	loc[i] = 'X'
for line in f.readlines():
	max = 0
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
		# print(lrow,rrow,lcol,rcol)
	max = rrow * 8 + rcol
	loc.pop(max)
for key in loc:
	if (key + 1) not in loc and (key - 1) not in loc:
		print(key) 