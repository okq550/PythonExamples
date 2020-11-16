# # Solution 1:
# # O(n^2) Time | O(n) Space
# def rotateImage(array):
#     newArray = []
#     for col in range(0, 3):
#         temp = []
#         for row in reversed(range(0, 3)):
#             temp.append(array[row][col])
        
#         newArray.append(temp)
#     return newArray
    
# Solution 2:
def rotateImage(array, n):
    for i in range(0, n):
        for j in range(i, n):
                swap(i, j, array)
    
    for i in range(0, n):
        for j in range(0, n // 2):
                swap(i, (n - 1) - j, array)
    return array
    
def swap(i, j, array):
    array[i][j], array[j][i] = array[j][i], array[i][j]
    
array = [[1,2,3], 
         [4,5,6], 
         [7,8,9]]
result = rotateImage(array, len(array))
print(result)