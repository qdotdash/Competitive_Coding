class QueueArray:
	def __init__(self):
		self.queue = []
		self.length = 0
		self.front = None
		self.back = None

	def enqueue(self, value):
		self.queue.append(value)
		self.length += 1
		if(self.front==None):
			self.front = 0
			self.back = 0
		else:
			self.back += 1

	def dequeue(self):
		if(self.front==None):
			print("No elements")
			return
		self.queue.pop(0)
		self.back -= 1
		self.length -= 1
		if(self.back==-1):
			self.back = None
			self.front = None

	def peek(self):
		if(self.front==None):
			print("No elements")
			return
		print(self.queue[0])

	def traverse(self):
		if(self.front==None):
			print("No elements")
			return
		for i in self.queue:
			print(i)

qu = QueueArray()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.traverse()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.traverse()
qu.enqueue(101)
qu.enqueue(102)
qu.enqueue(103)
qu.enqueue(104)
qu.traverse()
print("peek")
qu.peek()






