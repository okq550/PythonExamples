string = 'aaaaaaaaaaaaaaabbcccccaaa'
output = []
length = 1
for i in range(1, len(string)):
    currentChar = string[i]
    previouseChar = string[i - 1]
    if currentChar != previouseChar or length == 9:
        output.append(str(length))
        output.append(previouseChar)
        length = 0
    
    length += 1

output.append(str(length))
output.append(string[len(string) - 1])

output = ''.join(output)
 
print(output)