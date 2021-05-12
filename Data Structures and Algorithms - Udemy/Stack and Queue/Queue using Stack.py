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

class QueueUsingStack:
	def __init__(self):
		self.stack1 = StackLinkedList()
		self.stack2 = StackLinkedList()
	
	def enqueue(self, value):
		if(self.stack1.length==0):
			self.stack1.push(value)
		else:
			temp = self.stack1.top
			while(temp!=None):
				self.stack2.push(temp.value)
				temp = temp.next
				self.stack1.pop()
			self.stack2.push(value)

			temp = self.stack2.top
			while(temp!=None):
				self.stack1.push(temp.value)
				temp = temp.next
				self.stack2.pop()
			
		
	def dequeue(self):
		if(self.stack1.length==0):
			print("No elements in queue")
		else:
			print(self.stack1.top.value, " dequeued")
			self.stack1.pop()
		
	def traverseQueue(self):
		self.stack1.traverse()


queueUsingStack = QueueUsingStack()
queueUsingStack.enqueue(1)
queueUsingStack.enqueue(2)	
queueUsingStack.enqueue(3)	
queueUsingStack.enqueue(4)	
queueUsingStack.enqueue(5)	
queueUsingStack.traverseQueue()
queueUsingStack.dequeue()
queueUsingStack.dequeue()
queueUsingStack.traverseQueue()
queueUsingStack.dequeue()
queueUsingStack.dequeue()
queueUsingStack.dequeue()
queueUsingStack.dequeue()
queueUsingStack.dequeue()
queueUsingStack.dequeue()
queueUsingStack.traverseQueue()
queueUsingStack.enqueue(10)
queueUsingStack.enqueue(20)	
queueUsingStack.enqueue(30)	
queueUsingStack.enqueue(40)	
queueUsingStack.enqueue(50)
queueUsingStack.traverseQueue()





