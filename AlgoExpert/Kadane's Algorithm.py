# # Solution 1
# # O(n) Time | O(1) Space
# def kadanesAlgorithm(array):
#     sumsArray = [0 for x in range(len(array))]
#     sumsArray[0] = array[0]
#     maxSum = array[0]
#     for i in range(1, len(array)):
# 		if array[i] > array[i] + sumsArray[i - 1]:
# 			sumsArray[i] = array[i]
# 		else:
# 			sumsArray[i] = array[i] + sumsArray[i - 1]

# 		if sumsArray[i] > maxSum:
# 			maxSum = sumsArray[i]
#     return maxSum

# O(n) Time | O(1) Space.
def kadanesAlgorithm(array):
    maxAtIndx = array[0]
    maxSums = array[0]
    for num in array[1:]:
		# Return the miumum number between the number and the previouse sum + number
        maxAtIndx = max(num, maxAtIndx + num)
		# Update the max sums so far to be either the original max sums or the new max of the current number.
        maxSums = max(maxSums, maxAtIndx)
    return maxSums

array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
result = kadanesAlgorithm(array)
print(result)