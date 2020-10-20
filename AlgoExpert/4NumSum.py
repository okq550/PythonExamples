# Brute force method
# O(n^4)
def fourNumberSum(array, targetSum):
    array.sort()
    resultArray = []
    for i in range(0, len(array)):
        iElement = array[i]
        for j in range(i + 1, len(array)):
            jElement = array[j]
            for k in range(j + 1, len(array)):
                kElement = array[k]
                for l in range((k + 1), len(array)):
                    lElement = array[l]
                    sumElements = iElement + jElement + kElement + lElement
                    if sumElements == targetSum:
                        subResultArray = [array[i], array[j], array[k], array[l]]
                        resultArray.append(subResultArray)
    return resultArray

# Use left, right pointers
# O(n^2)
def fourNumberSum(array, targetSum):
    resultArray = []
    pairsArray = []
    dictionary = dict()
    array.sort()
    
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            pairSum = array[i] + array[j]
            pairArray = [array[i], array[j]]
            dictionary[pairSum] = pairArray
            # print(str(array[i]) + " " + str(array[j]))
    print(dictionary) 
    
    # left = 0
    # right = len(dictionary.keys()) - 1
    # for pair in dictionary:
    #     print(pair)
    #     if dictionary[]
    
    return pairsArray


array = [7, 6, 4, -1, 1, 2]
print(fourNumberSum(array, 16))