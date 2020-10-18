# # Brute force method
# def threeNumberSum(array, targetSum):
#     counter = 0
#     resultArray = []
#     for i in range(0, len(array)):
#         iElement = array[i]
#         for j in range(i + 1, len(array)):
#             jElement = array[j]
#             for k in range(j + 1, len(array)):
#                 kElement = array[k]
#                 sumElements = iElement + jElement + kElement
#                 if sumElements == targetSum:
#                     subResultArray = sorted([array[i], array[j], array[k]])
#                     resultArray.append(subResultArray)
#     return sorted(resultArray)

#Use pointers
def threeNumberSum(array, targetSum):
    # array = sorted(array)
    array.sort()
    resultArray = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                resultArray.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
        
    return resultArray
        

array = [12, 3, 1, 2, -6, 5, -8, 6]
print(threeNumberSum(array, -4))
