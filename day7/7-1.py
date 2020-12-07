
my_bag = 'shiny gold'
COUNT = 0



def loop(bags, curr_bag, visited):
	global COUNT
	if curr_bag in visited:
		return
	visited.append(curr_bag)
	if curr_bag in bags:
		for other in bags[curr_bag]:
			loop(bags, other, visited)
	if curr_bag != my_bag:
		COUNT += 1

f = open("input7.txt", "r")
bags = {}
for line in f.readlines():
	bag_list = line.strip().split('contain')
	# print(bag_list)
	container = bag_list[0].split('bag')[0].rstrip(' ')
	# print(container)
	contained = bag_list[1].split(',')
	bags_contained = []
	for bag in contained:
		temp = bag.split('bag')[0].lstrip(' ')
		temp2 = temp.lstrip('0123456789').rstrip(' ')
		num = temp[:len(temp) - len(temp2)].rstrip(' ')
		temp2 = temp2.lstrip(' ')
		if num != 'n':
			num = int(num)
		if temp2 in bags:
			bags[temp2].append(container)
		else: bags[temp2] = [container]
		# bags_contained.append(temp2)
		# print(num, temp2)

print(bags)
loop(bags, my_bag, [])
print(COUNT)



	# print('contained are' + str(contained))

