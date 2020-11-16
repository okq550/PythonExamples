array = [0]
i = 0
length = len(array)
while i < length:
    if array[i] != 4:
        array.append(i + 1)
        i += 1
        length = len(array)
    else:
        break
        
print(array)