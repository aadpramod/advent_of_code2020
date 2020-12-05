import re

birth_year ='byr'
issue_year = 'iyr'
exp_year = 'eyr' 
height = 'hgt'
hair_color = 'hcl'
eye_color = 'ecl'
pid = 'pid' 
count = 0
data = ''
valid = 0
valid_eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

f = open("input4.txt", "r")
for line in f.readlines():
        if line == '\n':
                temp = data.replace('\n', ' ')
                temp = temp.split(' ')
                # print(temp)
                for val in temp:
                        # print(val)
                        if birth_year == val.split(':')[0]:
                                if len(val.split(':')[1]) != 4 or not (int(val.split(':')[1]) >= 1920 and int(val.split(':')[1]) <= 2002):
                                        print('A')
                                        break
                                valid +=1
                        elif issue_year == val.split(':')[0]:
                                if len(val.split(':')[1]) != 4 or not (int(val.split(':')[1]) >= 2010 and int(val.split(':')[1]) <= 2020):
                                        print('B')
                                        break
                                valid +=1
                        elif exp_year == val.split(':')[0]:
                                if len(val.split(':')[1]) != 4 or not (int(val.split(':')[1]) >= 2020 and int(val.split(':')[1]) <= 2030):
                                        print('C')
                                        break
                                valid +=1
                        elif height == val.split(':')[0]:
                                if 'cm' in val.split(':')[1]:
                                        num = int(val.split(':')[1].split('cm')[0])
                                        if not (num >= 150 and num <= 190):
                                                break
                                        valid +=1
                                elif 'in' in val.split(':')[1]:
                                        num = int(val.split(':')[1].split('in')[0])
                                        if not (num >= 59 and num <= 76):
                                                print('D')
                                                break
                                        valid +=1
                                else: break
                        elif hair_color == val.split(':')[0]:
                                test = val.split(':')[1]
                                if test[0] != '#':
                                        print('E')
                                        break
                                pattern = re.compile("[a-f0-9]")
                                if len(test) != 6 and re.findall(pattern, test) is None:
                                        print('E')
                                        break
                                valid +=1
                        elif eye_color == val.split(':')[0]:
                                if val.split(':')[1] not in valid_eyes:
                                        print('F')
                                        break
                                valid +=1
                        elif pid == val.split(':')[0]:
                                pid2 = val.split(':')[1]
                                pattern = re.compile("[0-9]")
                                if len(pid2) != 9 and re.findall(pattern,pid2) is None:
                                        print('G')
                                        break
                                valid +=1
                if valid == 7:
                        count += 1
                data = ''
                valid = 0
                continue
        else: data += line
temp = data.replace('\n', ' ')
temp = temp.split(' ')
# print(temp)
temp = data.replace('\n', ' ')
temp = temp.split(' ')
# print(temp)
for val in temp:
        # print(val)
        if birth_year == val.split(':')[0]:
                if len(val.split(':')[1]) != 4 or not (int(val.split(':')[1]) >= 1920 and int(val.split(':')[1]) <= 2002):
                        print('A')
                        break
                valid +=1
        elif issue_year == val.split(':')[0]:
                if len(val.split(':')[1]) != 4 or not (int(val.split(':')[1]) >= 2010 and int(val.split(':')[1]) <= 2020):
                        print('B')
                        break
                valid +=1
        elif exp_year == val.split(':')[0]:
                if len(val.split(':')[1]) != 4 or not (int(val.split(':')[1]) >= 2020 and int(val.split(':')[1]) <= 2030):
                        print('C')
                        break
                valid +=1
        elif height == val.split(':')[0]:
                if 'cm' in val.split(':')[1]:
                        num = int(val.split(':')[1].split('cm')[0])
                        if not (num >= 150 and num <= 190):
                                break
                        valid +=1
                elif 'in' in val.split(':')[1]:
                        num = int(val.split(':')[1].split('in')[0])
                        if not (num >= 59 and num <= 76):
                                print('D')
                                break
                        valid +=1
                else: break
        elif hair_color == val.split(':')[0]:
                test = val.split(':')[1]
                if test[0] != '#':
                        print('E')
                        break
                pattern = re.compile("[a-f0-9]")
                if len(test) != 6 and re.findall(pattern, test) is None:
                        print('E')
                        break
                valid +=1
        elif eye_color == val.split(':')[0]:
                if val.split(':')[1] not in valid_eyes:
                        print('F')
                        break
                valid +=1
        elif pid == val.split(':')[0]:
                pid2 = val.split(':')[1]
                pattern = re.compile("[0-9]")
                if len(pid2) != 9 and re.findall(pattern,pid2) is None:
                        print('G')
                        break
                valid +=1
if valid == 7:
        count += 1
print(count)
