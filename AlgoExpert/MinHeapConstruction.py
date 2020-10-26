# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
	def __init__(self, array):
		# Do not edit the line below.
		self.heap = self.buildHeap(array)

	def buildHeap(self, array):
		# Using Sift down method.
		# Get the first parent Idx
		#Loop backwards to the root, and siftDown the whole thing.
		firstParentIdx = (len(array) - 2) // 2 
		for currentIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		return array
			

	def siftDown(self, currentIdx, endIdx, heap):
		# Get the child one of the current node.
		# While child one is not a leaf, Because there is no need to sift down if the child is a leaf.
		# Get the child two of the current node, if its within the array, meaning if the parent has only two childs.
		# If child two index is valid and the child two value is less than child one value, Then its the indx to swap, other wise use child one Idx instead. (Get smallest child value indx).
		# Swap if the currentIdx value is > smallest child value.
		# Set the currentIdx to be the childOneIdx, Update the childOneIdx for the loop
		# If the smallest child value is not less than the curent (Its parent), Break.
		# 
		childOneIdx = currentIdx * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap] < heap[currentIdx]:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				return

	def siftUp(self, currentIdx, heap):
		# Get the parent of current node.
		# While we did not pass the root of the heap and the current node value is greater than its parent,
		# Swap the current with the parent, 
		# The current now was the parent, Get it's parent again and continue till we reach the root.
		parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2

	def peek(self):
		# Return the Min/Max value of the heap,
		# Which is the root of the heap.
		return self.heap[0]
		pass

	def remove(self):
		# Swap the root with the last element.
		# Pop the last element.
		# Sift down starting from the top til the end of the heap.
		# Return the poped element (Min/Max value in the heap).
		self.swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return valueToRemove

	def insert(self, value):
		# Insert the element in last position,
		# Start sifting up from that last position.
		self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)
	
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]


def isMinHeapPropertySatisfied(array):
	for currentIdx in range(1, len(array)):
		parentIdx = (currentIdx - 1) // 2
		if array[parentIdx] > array[currentIdx]:
			return False
	return True

minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
minHeap.insert(76)
print(isMinHeapPropertySatisfied(minHeap.heap))
print(minHeap.peek(), -5)
minHeap.remove()
print(isMinHeapPropertySatisfied(minHeap.heap))
print(minHeap.peek(), 2)
minHeap.remove()
print(isMinHeapPropertySatisfied(minHeap.heap))
print(minHeap.peek(), 6)
minHeap.insert(87)
print(isMinHeapPropertySatisfied(minHeap.heap))