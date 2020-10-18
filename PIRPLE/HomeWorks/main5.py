#Generate a range from 1 to 100
for num in range(1, 101):
    if num % 3 and num % 5:
        print('FizzBuzz')
    elif num % 3:
        print('Fizz')
    elif num % 5:
        print('Buzz')

    #Prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print('Prime')
