class Array:	
	def __init__(self):
		self.length = 0
		self.array = {}

	def push(self, element):
		self.array[self.length] = element
		self.length += 1

	def pop(self):
  		lastItem = self.array[self.length-1]
  		del self.array[self.length-1]
  		self.length -= 1
  		return lastItem

	def delete(self, index):
		if(index>self.length-1 or index<0):
			print("Invalid index")
			return -1
		else:
			removedItem = self.array[index]
			self.shiftLeft(index)
			return removedItem

	def shiftLeft(self, index):
		for x in range(index, self.length-1):
			self.array[x] = self.array[x+1]
		del self.array[self.length-1]


array1 = Array()
array1.push(1)
array1.push(2)
array1.push(4)
array1.pop()
print(array1.array)
array1.push(3)
array1.push(4)
print(array1.array)
array1.push(7)
array1.push(6)
print(array1.array)
array1.delete(4)
print(array1.array)