class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class StackLinkedList:
	def __init__(self):
		self.top = None
		self.length = 0

	def push(self, value):
		newNode = Node(value)
		newNode.next = self.top
		self.top = newNode
		self.length += 1

	def pop(self):
		if(self.top==None):
			print("No elements")
			return
		popNode = self.top
		self.top = self.top.next
		self.length -= 1

	def peek(self):
		if(self.top==None):
			print("No elements")
			return
		peekNode = self.top
		print(peekNode.value)

	def traverse(self):
		if(self.top==None):
			print("No elements")
			return
		traverseNode = self.top
		while(traverseNode!=None):
			print(traverseNode.value)
			traverseNode = traverseNode.next

stl = StackLinkedList()
stl.push(4)
stl.push(3)
stl.push(2)
stl.push(1)
stl.traverse()
stl.pop()
stl.pop()
stl.traverse()
stl.push(100)
stl.push(101)
stl.push(102)
stl.push(103)
stl.traverse()
stl.peek()
stl.traverse()

