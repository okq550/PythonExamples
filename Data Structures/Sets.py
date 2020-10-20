mySet1 = set([1, 2, 3, 4, 5])
mySet2 = {1, 2}

mySet2.add(3)
mySet2.add(4)
mySet2.add(5)

mySet2.remove(5)

for element in mySet2:
    print(True if element % 2 else False)

mySet = mySet1.union(mySet2)
print(mySet)

mySet = mySet1.intersection(mySet2)
print(mySet)