# # Solution 1:
# # O(n) Time | O(1) Space
# def isPalindrome(string):
#     isPalindromeFlag = True
#     strSize = len(string)
#     i = 0
	
#     if strSize == 0:
#         return isPalindromeFlag
    
#     while isPalindromeFlag and i < strSize - (i + 1):
#         if string[i] != string[strSize - (i + 1)]:
#             isPalindromeFlag = False
#         i += 1
#     return isPalindromeFlag

# result = isPalindrome("abcdcba")
# print(result)

# Solution 2:
# O(n^2) Time | O(n) Space
def isPalindrome(string):
    reversedString = ''
    for i in reversed(range(len(string))):
        reversedString += string[i]
    
    return string == reversedString

result = isPalindrome("abcdcba")
print(result)