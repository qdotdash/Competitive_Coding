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
		self.previous = None

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
			newNode.previous = self.tail
			self.tail = newNode
			self.length += 1
		print("Value : ", value, " Appended")

	def prepend(self, value):
		if(self.length==0):
			self.firstValue(value)
		else:
			newNode = Node(value)
			newNode.next = self.head
			self.head.previous = newNode
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
			initialNode = self.traverseToIndex(index-1)
			finalNode = initialNode.next

			initialNode.next = insertNode
			insertNode.previous = initialNode

			insertNode.next = finalNode
			finalNode.previous = insertNode

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
				self.head.previous = None
				self.length-=1
				print("Value at ", index, " Removed")
			elif(index>0 and index<self.length-1):
				deletionNode = self.traverseToIndex(index)
				if(index==self.length-1):
					self.tail = deletionNode.previous
				deletionNode.previous.next = deletionNode.next
				deletionNode.next.previous = deletionNode.previous
				deletionNode.next = None
				deletionNode.previous = None
				self.length-=1
				print("Value at ", index, " Removed")
			else:
				print("Enter a value from ", 1, " to ", self.length-1)

	def reverse(self):
		if(self.tail!=None):
			reverseList = []
			reverseTraversalNode = self.tail
			while(reverseTraversalNode!=None):
				reverseList.append(reverseTraversalNode.value)
				reverseTraversalNode = reverseTraversalNode.previous
			print(reverseList)
		else:
			print("List is Empty")



MyLinkedList = LinkedList(0)
MyLinkedList.traverse()
MyLinkedList.append(1)
MyLinkedList.traverse()
MyLinkedList.append(2)
MyLinkedList.traverse()
MyLinkedList.append(3)
MyLinkedList.traverse()
MyLinkedList.append(4)
MyLinkedList.traverse()
MyLinkedList.prepend(-1)
MyLinkedList.traverse()
MyLinkedList.prepend(-2)
MyLinkedList.traverse()
MyLinkedList.prepend(-3)
MyLinkedList.traverse()
MyLinkedList.insert(1, 999)
MyLinkedList.traverse()
MyLinkedList.insert(222, 3)
MyLinkedList.traverse()
MyLinkedList.insert(8, 1000)
MyLinkedList.traverse()
MyLinkedList.insert(1, 9999)
MyLinkedList.traverse()
MyLinkedList.reverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(5)
MyLinkedList.traverse()
MyLinkedList.remove(100)
MyLinkedList.traverse()
MyLinkedList.remove(6)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.remove(0)
MyLinkedList.traverse()
MyLinkedList.insert(4, 2000)
MyLinkedList.traverse()
MyLinkedList.insert(1, 2001)
MyLinkedList.traverse()
MyLinkedList.append(666)
MyLinkedList.traverse()
MyLinkedList.prepend(-666)
MyLinkedList.traverse()
MyLinkedList.remove(5)
MyLinkedList.traverse()
MyLinkedList.reverse()











