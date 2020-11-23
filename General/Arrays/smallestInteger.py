def firstMissingPositive(nums) -> int:
        if 1 not in nums:
            return 1
        
        for i in range(1,len(nums)+1):
            mySet = set(nums)
            if i > 0 and i not in mySet:
                return i
            
            
array = [-1, 0, 1, 2, 3, 4]
output = firstMissingPositive(array)
print(output)