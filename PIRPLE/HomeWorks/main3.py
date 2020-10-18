def equalityCheck(num1, num2, num3):
    #For integer cascading for all input variables:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)

    #Comparing pairs, if non is equal to another then return False, else return True
    if num1!=num2 and num1!=num3 and num2!=num3:
        return False
    else:
        return True

print('Result is:')
print(equalityCheck(5,4,"5"))