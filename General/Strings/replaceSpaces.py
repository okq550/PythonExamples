string = 'Mr John Smith'

newString = string.replace(' ', '%20')

print(newString)
exit()

array = string.split(' ')
newString = ''

for i in range(0, len(array)):
    newString += array[i] + '20%'

print(newString)