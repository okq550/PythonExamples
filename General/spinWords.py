str = 'Hey fellow warriors'
newStrList = []

for word in str.split(' '):
    if len(word) >= 5:
        newStrList.append(word[::-1]) 
    else:
        newStrList.append(word)

separator = ' '
newStr = separator.join(newStrList)

# def spin_words(sentence):
#     # Your code goes here
#     return ' ' . join([x[::-1] if len(x)>5 else x for x in sentence.split(' ')])

# print(spin_words("hello fellow warriors"))