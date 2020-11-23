def arrayOfProducts(array):
    products = [1 for x in range(len(array))]
    arrayLength = len(array) - 1
    currentIdx, endIdx, leftIdx, rightIdx = 0, arrayLength, 0, arrayLength

    while currentIdx <= endIdx:
        while leftIdx <= rightIdx:
            if currentIdx == leftIdx:
                leftIdx += 1
            elif leftIdx != rightIdx:
                products[currentIdx] *= array[leftIdx] * array[rightIdx]
                leftIdx += 1
                rightIdx -= 1
            else:
                leftIdx+= 1
        currentIdx += 1
    
    return products

array = [5, 1, 4, 2]
output = arrayOfProducts(array)
print(output)
