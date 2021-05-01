class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Queue:
	def __init__(self):
		self.front = None
		self.rear = None
		self.length = 0
		print("The queue has been initialised")

	def enqueue(self, value):
		newNode = Node(value)
		if(self.length==0):
			self.front = self.rear = newNode
		else:
			newNode.next = self.rear
			self.rear = newNode
		self.length += 1

	def dequeue(self):
		if(self.length==0):
			print("No elements in the queue")
		elif(self.length==1):
			print("dequeued : ", self.front.value)
			self.front = self.rear = None
			self.length = 0
		else:
			temp = self.rear
			while(temp.next!=self.front):
				temp = temp.next
			self.front = temp
			self.front.next = None
			self.length -= 1

	def traverseQueue(self):
		if(self.length==0):
			print("No elements in the queue")
		else:
			queueList = []
			temp = self.rear
			while(temp!=None):
				queueList.append(temp.value)
				temp = temp.next
			print(queueList[::-1])
	
queue = Queue()
queue.enqueue(5)
queue.traverseQueue()
queue.dequeue()
queue.dequeue()
queue.traverseQueue()
queue.enqueue(43)
queue.enqueue(56)
queue.enqueue(86)
queue.traverseQueue()
queue.dequeue()
queue.traverseQueue()



	 