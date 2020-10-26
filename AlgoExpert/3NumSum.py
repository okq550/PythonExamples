# # Brute force method
# def threeNumberSum(array, targetSum):
#     array.sort()
#     resultArray = []
#     for i in range(0, len(array)):
#         iElement = array[i]
#         for j in range(i + 1, len(array)):
#             jElement = array[j]
#             for k in range(j + 1, len(array)):
#                 kElement = array[k]
#                 sumElements = iElement + jElement + kElement
#                 if sumElements == targetSum:
#                     subResultArray = [array[i], array[j], array[k]]
#                     resultArray.append(subResultArray)
#     return resultArray

# Use left, right pointers
# O(n^2)
def threeNumberSum(array, targetSum):
    resultArray = []
    array.sort()
    leftIndx = 0
    rightIndx = 0
    for currentIndx in range(0, len(array) - 1):
        leftIndx = currentIndx + 1
        rightIndx = len(array) - 1
        while leftIndx < rightIndx:
            currentSum = array[currentIndx] + array[leftIndx] + array[rightIndx]
            if currentSum == targetSum:
                resultArray.append([array[currentIndx], array[leftIndx], array[rightIndx]])
                leftIndx += 1
                rightIndx -= 1
            elif currentSum > targetSum:
                rightIndx -= 1
            else:
                leftIndx += 1
    return resultArray


array = [12, 3, 1, 2, -6, 5, -8, 6]
print(threeNumberSum(array, 0))