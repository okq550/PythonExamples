# Solution 1
# O(n^2) Time | O(1)
# input = [1,2,3,4]
# output = [1, 1, 1, 1]

# for i in range(0, len(input)):
#     for j in range(0, len(input)):
#         if i != j:
#             # if not output[j]:
#             #     output.append(input[j])
#             # else:
#             output[i] *= input[j]

# Solution 2
# O(2n) Time | O(1) Space
input = [1,2,3,4]
# output = []

# allProduct = 1
# for i in range(0, len(input)):
#     allProduct *= input[i]

# for i in range(0, len(input)):
#     output.append(int(allProduct / input[i]))

# print(output)

# Solution 3
# O(3n) Time | O(3) Space
# input = [1,2,3,4]
# left_products = [1 for x in range(len(input))]
# right_products = [1 for x in range(len(input))]
# output = [1 for x in range(len(input))]

# for i in range(1, len(input)):
#     left_products[i] = input[i - 1] * left_products[i - 1]
    
# for i in range(len(input) - 2, -1, -1):
#     right_products[i] = input[i + 1] * right_products[i + 1]

# for i in range(len(input)):
#     output[i] = left_products[i] * right_products[i]

# # print(left_products)
# # print(right_products)
# print(output)


# Solution 4
# O(2n) Time | O(1) Space
input = [1,2,3,4]
R = 1
output = [1 for x in range(len(input))]

for i in range(1, len(input)):
    output[i] = input[i - 1] * output[i - 1]
    
for i in range(len(input) - 1, -1, -1):
    print(i, R)
    output[i] = output[i] * R
    R *= input[i]

print(output)