class StackArray:
	def __init__(self):
		self.stack = []
		self.length = 0
		self.top = None

	def push(self, value):
		self.stack.append(value)
		self.length = self.length + 1
		self.top = self.length-1

	def pop(self):
		if(self.length==0):
			print("Empty Stack")
			return
		self.stack.pop(self.length-1)
		self.length = self.length - 1
		self.top = self.length-1

	def peek(self):
		if(self.length==0):
			print("Empty Stack")
			return
		print(self.stack[self.top])

	def lookup(self, index):
		if(index>self.top):
			print("Out of bounds")
			return
		print(self.stack[index])

	def traverse(self):
		if(self.length==0):
			print("No Elements")
			return
		for x in self.stack:
			print(x," ")

stackArray = StackArray()
stackArray.push(4)
stackArray.push(3)
stackArray.push(2)
stackArray.push(1)
stackArray.traverse()
stackArray.pop()
stackArray.pop()
stackArray.traverse()
stackArray.pop()
stackArray.pop()
stackArray.traverse()
stackArray.push(100)
stackArray.push(101)
stackArray.push(102)
stackArray.push(103)
stackArray.traverse()
stackArray.peek()
stackArray.traverse()


