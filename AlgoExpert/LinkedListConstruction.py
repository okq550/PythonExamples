# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
			self.head = node
			self.tail = node
			return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
			self.setHead(node)
			return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
		# Nothing to do here
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		
		#Remove the new node pointers and update it's next/prev nodes.
		self.remove(nodeToInsert)
		
		# Update the pointer of newly insertd node in relationship with the current node.
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		
		# If the current node is head, otherwise update the previous of current's next to point at the new node.
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		
		#Update the current node prev pointer to new node.
		node.prev = nodeToInsert
			 
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		
		self.remove(nodeToInsert)
		
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
			
		node.next = nodeToInsert
		
    def insertAtPosition(self, position, nodeToInsert):
        # Inserting a new head
		if position == 1:
			self.setHead(nodeToInsert)
			return
		
		# Traverse through the list and insert the node:
		node = self.head
		currentPosition = 1
		while node is not None and currentPosition != position:
			node = node.next
			currentPosition += 1
		
		# Once we break out the loop, either we found the node or we are at the tail.
		# If node is found, then new node will be inserted before current node. Else set it as a new tail.
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        currentNode = self.head
		while currentNode is not None:
			willRemoveNode = currentNode
			currentNode = currentNode.next
			if willRemoveNode.value == value:
				self.remove(willRemoveNode)

    def remove(self, node):
        if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		
		self.removeNodeLinks(node)

    def containsNodeWithValue(self, value):
		currentNode = self.head
		isFound = False
		while not isFound:
			if currentNode.value == value:
				return True
			if currentNode.next is not None:
				currentNode = currentNode.next
			else:
				return False
	
	def removeNodeLinks(self, node):
		if node.prev is not None:
			node.prev.next = node.next
		
		if node.next is not None:
			node.next.prev = node.prev
			
		node.prev = None
		node.next = None