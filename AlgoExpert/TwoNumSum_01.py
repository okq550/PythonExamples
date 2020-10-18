# def twoNumberSum(array, targetSum):
#     outputList = []
#     for i in range(len(array)):
#         for j in range(len(array)):
#             if i != j:
#                 numInI = array[i]
#                 numInJ = array[j]
#                 sumIandJ = numInI + numInJ
#                 isIAddedToOutput = numInI in outputList
#                 isJAddedToOutput = numInJ in outputList
#                 if sumIandJ == targetSum and not isIAddedToOutput and not isJAddedToOutput:
#                     outputList.append(numInI)
#                     outputList.append(numInJ)
#     return outputList

# def twoNumberSum(array, targetSum):
#     hashTable = dict()
#     for x in array:
#         y = targetSum - x
#         if y in hashTable:
#             return [x, targetSum - x]
#         else:
#             hashTable[x] = True
#     return []

# def twoNumberSum(array, targetSum):
#     firstIndex = 0
#     lastIndex = len(array) - 1
#     array.sort()
#     for num in array:
#         potentialSum = array[firstIndex] + array[lastIndex]
#         if potentialSum == targetSum:
#             return[array[firstIndex], array[lastIndex]]
#         elif potentialSum > targetSum:
#             lastIndex -=1
#         else:
#             firstIndex +=1
#     return []

# inputList = [5, 2, 1, 3]
# resultList = twoNumberSum(inputList, 4)
# print(resultList)


# array = [x for x in range(10)]
# print(array)

# for i in range(0, 10):
#     for j in range(i + 1, 10):
#         print(str(array[i]) + str(array[j]), end=' ')
#     print()