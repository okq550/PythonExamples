# # Solution 1 - While
# # O(log(n)) Time | O(1) Space
# import math

# def binarySearch(array, target):
#     leftIdx = 0
#     rightIdx = len(array) - 1
#     midIdx = math.floor(rightIdx - leftIdx)
	
#     while leftIdx <= rightIdx:
#         if target > array[midIdx]:
#             leftIdx = midIdx + 1
#             midIdx = math.floor(rightIdx + leftIdx)
#         elif target < array[midIdx]:
#             rightIdx = midIdx - 1
#             midIdx = math.floor(rightIdx + leftIdx)
#         else:
#             return midIdx
#     return -1


# # Solution 1 - Recursion
# # O(log(n)) Time | O(log(n)) Space
# def binarySearch(array, target):
#     return binarySearchHelper(array, target, 0, (len(array) - 1) // 2, len(array) - 1)


# def binarySearchHelper(array, target, leftIdx, midIdx, rightIdx):
# 	if leftIdx > rightIdx:
# 		return -1
	
# 	if array[midIdx] == target:
# 		return midIdx
# 	elif target < array[midIdx]:
# 		rightIdx = midIdx - 1
# 		midIdx = (rightIdx + leftIdx) // 2
# 		return binarySearchHelper(array, target, leftIdx, midIdx, rightIdx)
# 	elif target > array[midIdx]:
# 		leftIdx = midIdx + 1
# 		midIdx = (rightIdx + leftIdx) // 2
# 		return binarySearchHelper(array, target, leftIdx, midIdx, rightIdx)

target = 33
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
result = binarySearch(array, target)
print(result)
