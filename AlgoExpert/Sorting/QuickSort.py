# Avg: O(nLog(n)) Time | O(Log(n))
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, startIdx, endIdx):
	
	if startIdx >= endIdx:
		return 
	
	pivotIdx = startIdx
	leftIdx = startIdx + 1
	rightIdx = endIdx
	
	while leftIdx <= rightIdx:
		if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
			swap(array, leftIdx, rightIdx)
		
		if array[leftIdx] <= array[pivotIdx]:
			leftIdx += 1
		
		if array[rightIdx] >= array[pivotIdx]:
			rightIdx -= 1
	
	swap(array, pivotIdx, rightIdx)
	isleftSubArraySmaller = (rightIdx - 1) - startIdx < endIdx - (rightIdx + 1)
	
	if isleftSubArraySmaller:
		quickSortHelper(array, startIdx, rightIdx - 1)
		quickSortHelper(array, rightIdx + 1, endIdx)
	else:
		quickSortHelper(array, rightIdx + 1, endIdx)
		quickSortHelper(array, startIdx, rightIdx - 1)
	
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]


array = [8, 5, 2, 9, 5, 6, 3]
result = quickSort(array)
print(result)