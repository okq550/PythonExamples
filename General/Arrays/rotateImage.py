def rotateImage(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            array[i][j], array[j][i] = array[j][i], array[i][j]
            
    for i in range(len(array)):
        for j in range(len(array) // 2):
            array[i][j], array[i][len(array) - 1 - j] = array[i][len(array) - 1 - j], array[i][j]

array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rotateImage(array)
print(array)