# [4, 7, 5]
def addOne(array):
    resultArray = [ 0 for x in range(len(array))]
    carryFlag = 1
    for i in range(len(array) - 1, -1, -1):
        total = array[i] + carryFlag
        if total == 10:
            carryFlag = 1
        else:
            carryFlag = 0
            resultArray[i] = total
            
    if carryFlag == 1:
        resultArray = [ 0 for x in range(len(array)+ 1)]
        resultArray[0] = 1
        
    return resultArray
        
arrayResult = addOne([9, 9, 9, 9])
print(arrayResult)