# 
# 

# return "etyB yliaD ehT”

string = "The Daily Byte"
words = string.split(' ')
output = ''
words.reverse()

for word in words:
    for letter in word[::-1]:
        output += letter
    output += ' '

print(output)