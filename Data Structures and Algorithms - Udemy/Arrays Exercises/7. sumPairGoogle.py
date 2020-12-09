list1 = [1, 2, 5, 6, 9, 11, 17] #minsum = 1 + 2 = 3 and maxsum = 11 + 17  = 28
sum1 = 17
length1 = len(list1)
list2 = [1, 2, 64, 11, 1, 9, 32]
length2 = len(list2)
sum2 = 3

#sorted
def loopingCombinations(list1): #O(1)
	for i in range(length1):
		for j in range(i+1, length1):
			if(list1[i]+list1[j] == sum1):
				return True
	return False


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




def dictionaryIfUnordered(list2): #O(n)
	mapOfList2 = {}
	for x in list2:
		if(x in mapOfList2):
			return True
		else:
			mapOfList2[sum2-x] = True

	return False

def binarySearchOrdered(list1): #binary search but with adding the mid and mid+1 to locate the given sum
	first = 0
	last = length1 - 1
	mid  = int((first + last)/2)
	print("sum1 = ", sum1)
	while(first<=last):
		tempSum = list1[mid] + list1[mid+1]
		print("combination check : ", list1[mid], list1[mid+1])
		if(tempSum == sum1):
			return True
		elif(tempSum > sum1):
			last = mid - 1
			mid = midCalculation(first, last)
		else:
			first = mid + 1
			mid = midCalculation(first, last)
	return False


def midCalculation(first, last):
	return int((first + last)/2)

print(loopingCombinations(list1))

print(startFromEnds(list1))

print(dictionaryIfUnordered(list2))

print("\n",list1,"\n")

print(binarySearchOrdered(list1),end='')
