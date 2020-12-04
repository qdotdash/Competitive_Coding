string = "fun&!! time"

newList = string.split()
maxLength = 0
maxLengthString = ""
for x in newList:
	length = 0
	for y in x:
		if(y.isalpha()):
			length+=1
	if(length>maxLength):
		maxLength = length
		maxLengthString = x

for m in maxLengthString:
	if(m.isalpha()):
		print(m,end='')