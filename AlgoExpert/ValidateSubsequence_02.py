def isValidSubsequence(array, sequence):
    for x in sequence:
        if x not in array:
            return False
    return True

array = [5, 1, 22, 25, 6, -1, 8, 10]
subsequence = [1, 6, -1, 10]

result = isValidSubsequence(array, subsequence)

print(result)