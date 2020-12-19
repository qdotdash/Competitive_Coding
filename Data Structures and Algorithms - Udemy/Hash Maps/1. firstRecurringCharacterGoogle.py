# unordered - first recurring number - inputs - list, output - the recurring integer and undefined if no such integer exists

list1 = [1,0,1,4,5,6]


def findFirstRecurringElement(list1): #Naive Solution O(n^2)
	length = len(list1)
	indexOfReccurrence = length
	FirstRecurringElement = None
	i = 0
	j = 1
	while(i<indexOfReccurrence):
		while(j<indexOfReccurrence):
			if(list1[i]==list1[j]):
				indexOfReccurrence = j
				FirstRecurringElement = list1[i]
				break
			else:
				j+=1
		i += 1
		j = i + 1

	return FirstRecurringElement

def findFirstRecurringElementHashMap(list1): # Using hash map O(n)
	traversedOnes = {}
	for elementInArray in list1:
		if(traversedOnes.get(elementInArray)):
			return elementInArray
		else:
			traversedOnes[elementInArray] = True

	return None

print(findFirstRecurringElement(list1))
print(findFirstRecurringElementHashMap(list1), end='')
