myDic = {'Name': 'Osamah', 'Age': 37, 'City': 'Amman'}

print(myDic['Name'])
print(myDic['Age'])
print(myDic['City'])

myDic['Address'] = 'Sweileh'

print(len(myDic))

for key in myDic.keys():
    print(key)
    
for value in myDic.values():
    print(value)

for key, value in myDic.items():
    print(key, value)