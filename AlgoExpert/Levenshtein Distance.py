# # Solution 1 - Not working
# def levenshteinDistance(str1, str2):
#     # matrix = [[0] * len(str1)] * len(str2)
#     # matrix = [[0] * len(str1) for i in range(len(str2))]
#     matrix = [[0] * len(str1) for _ in range(len(str2))]
    
#     print()
#     printArray(matrix)
#     print()
#     # print(matrix)
    
#     counter = -1
#     for i in range(0, len(str2)):
#         print()
#         for j in range(0, len(str1)):
#             print('row', i, ' column', j, ' cost: ', end = '')
#             print(str2[i], str1[j], ' ', end = '')
#             if str2[i] != str1[j]:
#                 matrix[i][j] = 1
    
#     for i in range(0, len(str2)):
#         for j in range(0, len(str1)):
#             if matrix[i][j] == 0:
#                 counter += 1
    
#     print('Counter: ', counter)
            
#     # print() 
#     # print()
#     # printArray(matrix)
#     # print()

# def printArray(array):
#     for row in array:
#         print()
#         for column in row:
#             print(column, end = ' ')

# Solution 2
# O(n * m) Time | O(n * m) Space
# n/m are lengths of input strings.
def levenshteinDistance(str1, str2):
	matrix = [ [x for x in range(len(str1) + 1)] for y in range(len(str2) + 1) ]
	
	for i in range(1, len(str2) + 1):
		matrix[i][0] = matrix[i - 1][0] + 1
	
	print(matrix)
	
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i - 1] == str1[j - 1]:
				# print('if ', str2[i - 1], ' == ', str1[j - 1])
				matrix[i][j] = matrix[i -1][j - 1]
			else:
				matrix[i][j] =  1 + min([matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]])
				
	return matrix[-1][-1]

str1 = 'abc'
str2 = 'yabcd'

result = levenshteinDistance(str1, str2)

print(result)
