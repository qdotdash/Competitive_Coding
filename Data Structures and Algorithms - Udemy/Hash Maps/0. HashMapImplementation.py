'''
Things learnt

1. [[]] * 10 means the the inner list is copy of 10 same lists and values also changes same for all
2.

'''


class HashMap:
	def __init__(self, size):				# hashing table (0-size) 
		self.HashMapList = [-1] * size

	def __hash(self, key):	# key -> memory address in hashing table  ---- in real life hash -> some mapping -> memory address
		hash = 0
		length = len(key)
		for i in range(length):
			hash = (hash + ord(key[i]) * i) % len(self.HashMapList)
		return hash

	def set(self, key, value):
		memoryAddress = self.__hash(key) # memory address from key

		if(self.HashMapList[memoryAddress]==-1):	# if -1 or empty initialise it as list
			self.HashMapList[memoryAddress] = []
		else:
			for checkIfKeyAlreadyPresent in self.HashMapList[memoryAddress]: #if key already inserted then don't input value
				if(checkIfKeyAlreadyPresent[0]==key):
					return

		self.HashMapList[memoryAddress].append([key, value]) # push to the inner list

	def get(self, key):
		memoryAddress = self.__hash(key)
		if(self.HashMapList[memoryAddress]!=-1):  #check if inner list present -> check if key in inner list
			for traverseInnerList in self.HashMapList[memoryAddress]:
				if(traverseInnerList[0]==key):
					return traverseInnerList[1]
		else:
			return -1

	def keys(self):
		tempList = self.HashMapList
		for x in tempList:
			if(x!=-1):
				for y in x:
					print(y[0])



myHashTable = HashMap(4)
myHashTable.set('grapes', 10000)
myHashTable.set('apples', 9)
myHashTable.set('sherin', 22)
myHashTable.set('alina', 21)
myHashTable.set('alina', 24) #not inserted, duplicate key
print(myHashTable.HashMapList)
print(myHashTable.get('alina'))
print(myHashTable.get('sherin'))
myHashTable.keys()