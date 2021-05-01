size = int(input())
arrayList = []
for i in range(size):
	arrayList.append(input())
N = int(input())
arrayList.sort()
tempN = N
flag = 0
for i in arrayList:
	if(tempN==1):
		print(i, end='')
		flag = 1
		break
	else:
		tempN -= 1


