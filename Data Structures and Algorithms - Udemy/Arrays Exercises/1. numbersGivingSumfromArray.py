#nums = []
#inputList = input().split() #input an unknown number of inputs as string and split and convert to int
#for x in inputList:
#	nums.append(int(x))
nums = []
temp = input()
temp = temp[1:len(temp)-1]
temp1 = temp.split(',')
for x in temp1:
	nums.append(int(x))
length = len(nums)
answer = "["
target = int(input())
flag = False
for i in range(0, length):
	x = nums[i]	
	for j in range(0, length):
		y = nums[j]
		if(x!=y):
			if(x+y==target):
				answer += str(i) + ',' + str(j) + ']'
				flag = True
				break
	if(flag):
		break

print(answer,end = '')