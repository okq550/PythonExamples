# # Brute force method
# # O(n^4)
# def fourNumberSum(array, targetSum):
#     array.sort()
#     resultArray = []
#     for i in range(0, len(array)):
#         iElement = array[i]
#         for j in range(i + 1, len(array)):
#             jElement = array[j]
#             for k in range(j + 1, len(array)):
#                 kElement = array[k]
#                 for l in range((k + 1), len(array)):
#                     lElement = array[l]
#                     sumElements = iElement + jElement + kElement + lElement
#                     if sumElements == targetSum:
#                         subResultArray = [
#                             array[i], array[j], array[k], array[l]]
#                         resultArray.append(subResultArray)
#     return resultArray

# Accumelate method
# Average: O(n^2) time | O(n^2) space
# Worst: O(n^3) time | O(n^2) space
def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets

array = [7, 6, 4, -1, 1, 2]
print(fourNumberSum(array, 16))
