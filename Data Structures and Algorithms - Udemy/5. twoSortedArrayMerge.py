def sort1(arr1, arr2):
	arr3 = []
	length1 = len(arr1)
	length2 = len(arr2)
	i = j = 0
	while(i<length1 and j<length2):
		if(arr1[i]<arr2[j]):
			arr3.append(arr1[i])
			i += 1
		else:
			arr3.append(arr2[j])
			j += 1
"""
the if else based on length fails because the first array that gets completed depends 
on the last element, not on the length of array
"""
		arr3.append(arr1[i])

	while(i<length1):				
		i += 1

	while(j<length2):
		arr3.append(arr2[j])
		j += 1

	return arr3

arr1 = [1, 3, 5, 7, 9, 11, 55, 67]
arr2 = [2, 4, 6, 8, 10, 12, 14 ,16, 19]
print(arr1)
print(arr2)
print(sort1(arr1, arr2))

