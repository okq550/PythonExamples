# Solution 1:
# O(n) time, O(1) space - Where n is the size of the input array.
def moveElementToEnd(array, toMove):
	rightPos = len(array) - 1
	leftPos = 0
	while leftPos < rightPos:
		if array[rightPos] != toMove and array[leftPos] == toMove:
			swap(array, leftPos, rightPos)
			rightPos -= 1
			leftPos += 1
		else:
			if array[rightPos] == toMove:
				rightPos -= 1
			else:
				leftPos += 1
	return array

# # Solution 2:
# # O(n) time, O(1) space - Where n is the size of the input array.
# def moveElementToEnd(array, toMove):
# 	left = 0
# 	right = len(array) - 1
# 	while left < right:
# 		while left < right and array[right] == toMove:
# 			right -= 1
		
# 		if array[left] == toMove:
# 			swap(array, left, right)
		
# 		left += 1
		
# 	return array

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

output = moveElementToEnd(array, toMove)
print(output)