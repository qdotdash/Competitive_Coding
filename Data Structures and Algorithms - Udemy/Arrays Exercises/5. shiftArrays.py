#When newlist = oldlist, both will get modified when one is edited !!!!!!!!!!!!!!!!!

nums = [1,2,3,4,5,6,7]
k = 3
length = len(nums)
temp = nums.copy()

def indexRet(index, length, k):
	newIndexVal = (i+k)%length
	return newIndexVal



for i in range(length):
	newIndex = indexRet(i, length, k)
	nums[newIndex] = temp[i]	

print(nums)