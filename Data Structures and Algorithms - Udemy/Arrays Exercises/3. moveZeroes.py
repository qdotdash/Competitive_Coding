nums = [0,0,3,0,1,0,3,12]
j=0
for i in range(len(nums)):
	if(nums[i]==0):
		j+=1
	elif(j!=0):
		nums[i-j]=nums[i]
		nums[i] = 0

print(nums)
