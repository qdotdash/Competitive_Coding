# unordered - first recurring number - inputs - list, output - the recurring integer and undefined if no such integer exists

list1 = [2,1,5,1,1]


def findFirstRecurringElement(list1):
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

print(findFirstRecurringElement(list1), end='')
