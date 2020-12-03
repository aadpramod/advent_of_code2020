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
print(nums)
for i in range(len(nums)):
	j = 1 + i
	print(i)
	while(j < len(nums)):
		k = j + 1
		while(k < len(nums)):
			if nums[i] + nums[j] + nums[k] == 2020:
				print(nums[i]*nums[j] * nums[k])
				done = True
				break
			if nums[i] + nums[j] + nums[k] > 2020:
				print(i, j,k, nums[i], nums[j],nums[k], nums[i] + nums[j] + nums[k], ' No match')
				break
			k += 1
		j += 1
		if nums[i] + nums[j] + nums[j+1] > 2020:
			print(i, j,j + 1, nums[i], nums[j], nums[j + 1], nums[i] + nums[j]+ nums[j+1], ' No match')
			break
	if done:
		break