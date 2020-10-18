sum = 0

# for i in range(10):
#     number = input('Please enter a number: ')
#     if int(number) % 2 == 0:
#         print('The number is even')
#     else:
#         print('This number is odd')
            
number = int(input('Please enter a number: '))
while number is not -1:
    if int(number) % 2 == 0:
        print('The number is even')
    else:
        print('This number is odd')
        
    number = int(input('Please enter a number: '))