my_bag = 'shiny gold'
COUNT = 0



def loop(bags, curr_bag):
	global COUNT
	num_bags = 0
	if curr_bag in bags:
		for num, other in bags[curr_bag]:
			num_bags += loop(bags, other) * num
	# print(curr_bag, num_bags)
	if curr_bag != my_bag and curr_bag != 'no other':
		num_bags +=1
	return num_bags


f = open("input7.txt", "r")
bags = {}
for line in f.readlines():
	bag_list = line.strip().split('contain')
	container = bag_list[0].split('bag')[0].rstrip(' ')
	contained = bag_list[1].split(',')
	bags_contained = []
	for bag in contained:
		temp = bag.split('bag')[0].lstrip(' ')
		temp2 = temp.lstrip('0123456789').rstrip(' ')
		num = temp[:len(temp) - len(temp2)].rstrip(' ')
		temp2 = temp2.lstrip(' ')
		if num != 'n':
			num = int(num)
		else: num = 0
		bags_contained.append((num, temp2))
	bags[container] = bags_contained

COUNT = loop(bags, my_bag)
print(COUNT)

