nums = []
done = False
f = open("input1.txt", "r")
line = f.readline()
while line != "":
	line = int(line.split()[0])
	nums.append(line)
	line = f.readline() 
f.close()
nums.sort()
for i in range(len(nums)):
	j = 1 + i
	print(i)
	while(j < len(nums)):
		if nums[i] + nums[j] == 2020:
			print(nums[i]*nums[j])
			done = True
			break
		if nums[i] + nums[j] > 2020:
			print(i, j,nums[i], nums[j], nums[i] + nums[j], ' No match')
			break
		j += 1
	if done:
		break