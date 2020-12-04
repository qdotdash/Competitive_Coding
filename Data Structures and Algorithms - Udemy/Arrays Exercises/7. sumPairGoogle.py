list1 = [1, 2, 5, 6, 9, 11, 17] #minsum = 1 + 2 = 3 and maxsum = 11 + 17  = 28
sum1 = 15
length1 = len(list1)
list2 = [1, 2, 64, 11, 1, 9, 32]
sum2 = 3

#sorted
def loopingCombinations(list1): #O(1)
	for i in range(length1):
		for j in range(i+1, length1):
			if(list1[i]+list1[j] == sum1):
				return True
	return False

print(loopingCombinations(list1))


def startFromEnds(list1): #O(n)
	indexValueMinimum = 0
	indexValueMaximum = length1-1
	indexValue1 = indexValueMinimum
	indexValue2 = indexValueMaximum
	while(indexValue1<indexValue2):
		obtainedSum = list1[indexValue1] + list1[indexValue2] 
		if(obtainedSum == sum1):
			return True
		elif(obtainedSum > sum1):
			indexValue2 -= 1
		else:
			indexValue1 += 1

	return False

print(startFromEnds(list1))


def dictionaryIfUnordered(list2):
	mapOfList2 = {}
	for x in list2:
		if(x in mapOfList2):
			return True
		else:
			mapOfList2[sum2-x] = True

	return False

print(dictionaryIfUnordered(list2),end='')