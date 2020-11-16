def sumOfTwo(a, b, target):
    components = dict()
    for num1 in a:
        components[target - num1] = True
    
    
    for num2 in b:
        if num2 in components.keys():
            return True
    
    return False

a = [-5, 0, 0, 32]
b = [9, 1, -2, 10]

result = sumOfTwo(a, b, -8)

print(result)
