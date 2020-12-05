birth_year ='byr'
issue_year = 'iyr'
exp_year = 'eyr' 
height = 'hgt'
hair_color = 'hcl'
eye_color = 'ecl'
pid = 'pid' 
count = 0
data = ''

f = open("input4.txt", "r")
for line in f.readlines():
	print(line)
        if line == '\n':
        	if birth_year in data and issue_year in data and exp_year in data and height in data and \
        	hair_color in data and eye_color in data and pid in data:
        		count += 1
        	data = ''
        	continue
        data += line

if birth_year in data and issue_year in data and exp_year in data and height in data and \
        	hair_color in data and eye_color in data and pid in data:
        		count += 1
print(count)
