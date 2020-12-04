nums = [-1]
totalsum = maxsum = nums[0]

for i in range(1, len(nums)):
	totalsum += nums[i]
	if(nums[i]>=totalsum):
		totalsum = nums[i]

	if(totalsum>=maxsum):
		maxsum = totalsum

print(maxsum,end = '')