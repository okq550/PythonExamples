# O(n) time | O(n) space
def isValidSubsequence(array, sequence):

    # Loop over the sequence as long as indcies are increasing
    for i in range(len(sequence)):
        currentElemnt = sequence[i]
        try:
            indexInArray = array.index(sequence[i], i)
        except ValueError:
            return False

        if indexInArray >= 0 and i <= indexInArray and sequence.count(sequence[i]) <= array.count(sequence[i]):
            i += 1
        else:
            return False
    return True


# # O(n) time | O(n) space
# def isValidSubsequence(array, sequence):
#     arrIdx = 0
#     seqIdx = 0
#     while arrIdx < len(array) and seqIdx < len(sequence):
#         if array[arrIdx] == sequence[seqIdx]:
#             seqIdx += 1
#         arrIdx += 1
#     return seqIdx == len(sequence)

# # O(n) time | O(n) space
# def isValidSubsequence(array, sequence):
#     seqIdx = 0
#     for value in array:
#         if seqIdx == len(sequence):
#             break
#         if sequence[seqIdx] == value:
#             seqIdx += 1
#     return seqIdx == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequenece = [1, 22, 25, 6, -1, -1]

print(isValidSubsequence(array, sequenece))
