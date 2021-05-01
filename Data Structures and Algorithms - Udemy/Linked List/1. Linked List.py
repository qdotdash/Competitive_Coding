class Node:		#class for each node
	def __init__(self, value):
		self.value  = value
		self.next = None


class LinkedList:	#Linklist class with functionalities
	def __init__(self, value):
		firstValue = Node(value)		# objects are naturally pointers when assigned
		self.head = firstValue
		self.tail = self.head
		self.length = 1					# COOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL

	def append(self, value):
		appendValue = Node(value)
		self.tail.next = appendValue
		self.tail = appendValue
		self.length += 1

	def prepend(self, value):
		prependValue = Node(value)
		prependValue.next = self.head
		self.head = prependValue
		self.length += 1

	def insert(self, index, value):
		newNode = Node(value)
		if(index==0):
			self.prepend(value)
			self.length+=1
			return
		if(index>self.length-1 or index<0):
			print("Out of bounds")
			return

		findIndexNode = self.traverseToIndex(index-1)
		newNode.next = findIndexNode.next
		findIndexNode.next = newNode
		self.length += 1

	def delete(self, index):
		if(self.length==0):
			print("Empty...")
			return
		if(index<0 or index>self.length-1):
			print("Deletion index out of bounds...")
			return
		if(index==0):
			if(self.length==1):
				self.head = self.tail = None
			else:
				self.head = self.head.next
		else:
			nodeBeforeDeleteNode = self.traverseToIndex(index-1)
			nodeBeforeDeleteNode.next = nodeBeforeDeleteNode.next.next
			if(index==self.length-1):
				self.tail = nodeBeforeDeleteNode
		self.length -= 1
		print("Deletion successful...")

	def traverse(self):
		wholeLinkList = []
		traversalNode = self.head
		while(traversalNode!=None):
			wholeLinkList.append(traversalNode.value)
			traversalNode = traversalNode.next
		print(wholeLinkList, " Head : ", self.head.value, " Tail : ", self.tail.value)

	def traverseToIndex(self, index):				# COOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL
		traversetoNode = self.head
		i=0
		while(i!=index):
			traversetoNode = traversetoNode.next
			i+=1
		return traversetoNode


Llist = LinkedList(0)
hasCreatedLinkList = True
Llist.append(1)
Llist.append(2)
Llist.append(3)
Llist.append(4)
Llist.append(5)
Llist.prepend(-1)
Llist.prepend(-2)
Llist.prepend(-3)
Llist.prepend(-4)
Llist.prepend(-5)
Llist.traverse()
Llist.delete(0)
Llist.traverse()
Llist.delete(9)
Llist.traverse()

choice = 1
while(choice!=0):
	choice = int(input("\n1 - Create\n2 - Append\n3 - Prepend\n4 - Traverse\n5 - Insert\n6 - Delete\nYour choice : "))
	if(choice==1):
		if(not hasCreatedLinkList):
			hasCreatedLinkList = True
			Llist = LinkedList(int(input("Enter Initial value : ")))
			print("Linklist created...")
		else:
			print("Linklist already created...")
	elif(choice==2 and hasCreatedLinkList):
		Llist.append(int(input("Enter value to append : ")))
		print("Append Successful")
	elif(choice==3 and hasCreatedLinkList):
		Llist.prepend(int(input("Enter value to prepend : ")))
		print("Prepend Successful")
	elif(choice==4 and hasCreatedLinkList):
		Llist.traverse()
	elif(choice==5 and hasCreatedLinkList):
		index = int(input("Enter the index : "))
		value = int(input("Enter the value : "))
		Llist.insert(index, value)
		print("Insertion Successful")
	elif(choice==6 and hasCreatedLinkList):
		Llist.delete(int(input("Enter the index : ")))
	elif(choice==0):
		print("Exiting...")
	elif(choice>=2 and choice<=6):
		print("No Linklist created, press 1")
	else:
		print("Invalid Choice")

