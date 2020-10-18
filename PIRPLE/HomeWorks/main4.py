#Initialize empty list as a start
myUniqueList = []
myLeftovers = []

def addThingsToRejectedList(myLeftovers, input):
    myLeftovers.append(input)

def addThingsToList(myUniqueList, input):
    #Add elements to a list
    # inputList.append(input)
    if input not in myUniqueList:
        myUniqueList.append(input)
        return True
    else:
        return False

inputVar = 1
#If adding to unique list is False then add it to rejected list:
if addThingsToList(myUniqueList, inputVar) is False:
    addThigsToListLeftOversResult = addThingsToRejectedList(myLeftovers, inputVar)
print('myUniqueList: ', myUniqueList)
print('myLeftovers: ', myLeftovers)

inputVar = 2
#If adding to unique list is False then add it to rejected list:
if addThingsToList(myUniqueList, inputVar) is False:
    addThigsToListLeftOversResult = addThingsToRejectedList(myLeftovers, inputVar)
print('myUniqueList: ', myUniqueList)
print('myLeftovers: ', myLeftovers)

inputVar = 3
#If adding to unique list is False then add it to rejected list:
if addThingsToList(myUniqueList, inputVar) is False:
    addThigsToListLeftOversResult = addThingsToRejectedList(myLeftovers, inputVar)
print('myUniqueList: ', myUniqueList)
print('myLeftovers: ', myLeftovers)

inputVar = 2
#If adding to unique list is False then add it to rejected list:
if addThingsToList(myUniqueList, inputVar) is False:
    addThigsToListLeftOversResult = addThingsToRejectedList(myLeftovers, inputVar)
print('myUniqueList: ', myUniqueList)
print('myLeftovers: ', myLeftovers)