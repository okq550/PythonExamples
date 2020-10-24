def levenshteinDistance(str1, str2):
    # matrix = [[0] * len(str1)] * len(str2)
    # matrix = [[0] * len(str1) for i in range(len(str2))]
    matrix = [[0] * len(str1) for _ in range(len(str2))]
    
    print()
    printArray(matrix)
    print()
    # print(matrix)
    
    counter = -1
    for i in range(0, len(str2)):
        print()
        for j in range(0, len(str1)):
            print('row', i, ' column', j, ' cost: ', end = '')
            print(str2[i], str1[j], ' ', end = '')
            if str2[i] != str1[j]:
                matrix[i][j] = 1
    
    for i in range(0, len(str2)):
        for j in range(0, len(str1)):
            if matrix[i][j] == 0:
                counter += 1
    
    print('Counter: ', counter)
            
    # print() 
    # print()
    # printArray(matrix)
    # print()

def printArray(array):
    for row in array:
        print()
        for column in row:
            print(column, end = ' ')

str1 = 'abc'
str2 = 'yabd'

levenshteinDistance(str1, str2)
