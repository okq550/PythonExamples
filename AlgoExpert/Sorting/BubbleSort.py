# # Solution 1
# # Best: O(n) Time | O(1) Space.
# # Avg: O(n^2) Time | O(1) Space.
# # Worst: O(n^2) Time | O(1) Space.
# def bubbleSort(array):
# 	swapsCounter = 0
# 	i = 0
# 	while i < len(array) - 1:
# 		if array[i] > array[i + 1]:
# 			swapsCounter += 1
# 			tmp = array[i + 1]
# 			array[i + 1] = array[i]
# 			array[i] = tmp
# 		i += 1
		
# 		if i == len(array) - 1:
# 			if swapsCounter > 0:
# 				i = 0
# 				swapsCounter = 0
# 			else:
# 				break
# 	return array

# Solution 2
# Best: O(n) Time | O(1) Space.
# Avg: O(n^2) Time | O(1) Space.
# Worst: O(n^2) Time | O(1) Space.
def bubbleSort(array):
	isSorted = False
	counter = 0
	while not isSorted:
		isSorted = True
		for i in range(len(array) - 1 - counter):
			if array[i] > array[i + 1]:
				swap(i , i + 1, array)
				isSorted = False
		counter += 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
 
 
array = [8, 5, 2, 9, 5, 6, 3]
result = bubbleSort(array)
print(result)