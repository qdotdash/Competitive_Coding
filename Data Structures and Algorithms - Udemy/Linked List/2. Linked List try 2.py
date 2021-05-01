'''
remember length property
traverse to index property
modifying length on change in link list
modifying head and tail on change in linklist
'''


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self, value):
		newNode = Node(value)
		self.head = self.tail = newNode
		self.length = 1
		print("Linked List created with initial value : ", value)

	def firstValue(self, value):
		newNode = Node(value)
		self.head = self.tail = newNode
		self.length = 1

	def append(self, value):
		if(self.length==0):
			self.firstValue(value)
		else:
			newNode = Node(value)
			self.tail.next = newNode
			self.tail = newNode
			self.length += 1
		print("Value : ", value, " Appended")

	def prepend(self, value):
		if(self.length==0):
			self.firstValue(value)
		else:
			newNode = Node(value)
			newNode.next = self.head
			self.head = newNode
			self.length += 1
		print("Value : ", value, " Prepended")

	def traverse(self):
		lList = []
		if(self.head!=None):
			traverseNode = self.head
			while(traverseNode!=None):
				lList.append(traverseNode.value)
				traverseNode = traverseNode.next
			print(lList, " length = ", self.length)
		else:
			print(lList, " List Empty, nothing to traverse")	

	def insert(self, index, value):
		if(self.length==0):
			print("Empty List for insertion")
			return

		if(index >0 and index < self.length):
			insertNode = Node(value)
			vantageNode = self.traverseToIndex(index-1)
			insertNode.next = vantageNode.next
			vantageNode.next = insertNode
			self.length += 1
			print("Value Inserted at index ", index)
		else:
			print("Enter a value from ", 1, " to ", self.length-1)

	def traverseToIndex(self, index):
		if(self.head!=None):
			traverseNode = self.head
			i=0
			if(index==0):
				return self.head

			while(i!=index):
				traverseNode = traverseNode.next
				i += 1

			return traverseNode

	def remove(self, index):
		if(self.head!=None):
			if(self.length==1 and index==0):
				self.head = self.tail = None
				self.length-=1
			elif(index==0):
				self.head = self.head.next
				self.length-=1
				print("Value at ", index, " Removed")
			elif(index>0 and index<self.length-1):
				vantageNode = self.traverseToIndex(index-1)
				if(index==self.length-1):
					self.tail = vantageNode
				vantageNode.next = vantageNode.next.next
				self.length-=1
				print("Value at ", index, " Removed")
			else:
				print("Enter a value from ", 1, " to ", self.length-1)

	def reverse(self):
		if(self.head==None):
			print("List is Empty")
		elif(self.length==1):
			self.traverse()
		else:
			self.initiateReversal()

	def initiateReversal(self):
		first = self.head
		second = first.next
		temp = None
		if(second.next!=None):
			temp = second.next
		first.next = None
		self.tail = self.head #repositioned self.head to end
		while(second!=None):
			second.next = first
			first = second
			second = temp
			if(second!=None):
				temp = temp.next
		self.head = first
		self.traverse()

MyLinkedList = LinkedList(0)
MyLinkedList.append(1)
MyLinkedList.append(2)
MyLinkedList.append(3)
MyLinkedList.append(4)
MyLinkedList.append(5)
MyLinkedList.append(6)
MyLinkedList.append(7)
MyLinkedList.traverse()
MyLinkedList.reverse()
# MyLinkedList = LinkedList(0)
# MyLinkedList.traverse()
# MyLinkedList.append(1)
# MyLinkedList.traverse()
# MyLinkedList.append(2)
# MyLinkedList.traverse()
# MyLinkedList.append(3)
# MyLinkedList.traverse()
# MyLinkedList.append(4)
# MyLinkedList.traverse()
# MyLinkedList.prepend(-1)
# MyLinkedList.traverse()
# MyLinkedList.prepend(-2)
# MyLinkedList.traverse()
# MyLinkedList.prepend(-3)
# MyLinkedList.traverse()
# MyLinkedList.insert(1, 999)
# MyLinkedList.traverse()
# MyLinkedList.insert(222, 3)
# MyLinkedList.traverse()
# MyLinkedList.insert(8, 1000)
# MyLinkedList.traverse()
# MyLinkedList.insert(1, 9999)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(5)
# MyLinkedList.traverse()
# MyLinkedList.remove(100)
# MyLinkedList.traverse()
# MyLinkedList.remove(6)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.remove(0)
# MyLinkedList.traverse()
# MyLinkedList.insert(4, 2000)
# MyLinkedList.traverse()
# MyLinkedList.insert(1, 2001)
# MyLinkedList.traverse()
# MyLinkedList.append(666)
# MyLinkedList.traverse()
# MyLinkedList.prepend(-666)
# MyLinkedList.traverse()
# MyLinkedList.remove(5)
# MyLinkedList.traverse()











