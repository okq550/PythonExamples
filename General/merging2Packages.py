#Merging 2 Packages
"""
Given a package with a weight limit limit and an array arr of item weights, implement a function getIndicesOfItemWeights 
that finds two items whose sum of weights equals the weight limit limit. Your function should return a pair [i, j] of the indices of the item weights, 
ordered such that i > j. If such a pair doesn’t exist, return an empty array.

Example:

input:  arr = [4, 6, 10, 15, 16],  lim = 21

output: [3, 1] # since these are the indices of the
               # weights 6 and 15 whose sum equals to 21
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 100
[input] integer limit

[output] array.integer

Analyze the time and space complexities of your solution.
"""

def get_indices_of_item_wights(arr, limit):
  discovered_weights_dict = {}
  
  for i in range(len(arr)):
    number = arr[i]
    complement = limit - number
    if complement not in discovered_weights_dict.keys():
      discovered_weights_dict[arr[i]] = i
    else:
      return [i, discovered_weights_dict[complement]]
  
  return []

# # result should be [3,1]
# result = get_indices_of_item_wights([4,6,10,15,16], 21)
# print(result)

# # result should be [1,0]
# result = get_indices_of_item_wights([4,4], 8)
# print(result)

# result should be []
result = get_indices_of_item_wights([9], 9)
print(result)