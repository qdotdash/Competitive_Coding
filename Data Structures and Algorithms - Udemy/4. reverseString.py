def reverseString1(stringValue): #reversing using function
	revString  = ""
	length = len(stringValue)
	for x in range(length-1, -1, -1):
		revString += stringValue[x]
	return revString

def reverseString2(stringValue): #reversing using slicing
	revString = stringValue[::-1] #creating a slice (end:begin:decrement) = (: : -1)
	return revString

stringValue = input()
print(reverseString1(stringValue))
print(reverseString2(stringValue))