# O(nlog(n)) Time | O(1) Space
def heapSort(array):
	buildMaxHeap(array)
	for endIdx in reversed(range(1, len(array))):
		swap(0, endIdx, array)
		siftDown(0, endIdx - 1, array)
	return array

def buildMaxHeap(array):
	firstParentIdx = (len(array) - 2) // 2
	for currentIdx in reversed(range(firstParentIdx + 1)):
		siftDown(currentIdx, len(array) - 1, array)

def siftDown(currentIdx, endIdx, array):
	childOneIdx = currentIdx * 2 + 1
	while childOneIdx <= endIdx:
		childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
		if childTwoIdx != -1 and array[childTwoIdx] > array[childOneIdx]:
			swapIdx = childTwoIdx
		else:
			swapIdx = childOneIdx
		
		if array[swapIdx] > array[currentIdx]:
			swap(swapIdx, currentIdx, array)
			currentIdx = swapIdx
			childOneIdx = currentIdx * 2 + 1
		else:
			return

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

array = [8, 5, 2, 9, 5, 6, 3]
result = heapSort(array)
print(result)