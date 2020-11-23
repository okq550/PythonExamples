# # Solution 1
# # O(n^2 * n!) Time | O(n * n!) Space
# # Time: we have n! permutations, n calls for the helper method and eash helper call has n time of operation (Copy arr, delete arr element)
# # Space: we have n! permutations with n length each.
# def getPermutations(array):
#     perm = []
#     perms = []
#     getPermutationsHelper(array, perm, perms)
#     return perms


# def getPermutationsHelper(arr, perm, perms):
#     if not len(arr) and len(perm):
#         perms.append(perm)
#     else:
#         for i in range(len(arr)):
#             newArr = arr[:i] + arr[i + 1:]
#             newPerm = perm[:] + [arr[i]]
#             getPermutationsHelper(newArr, newPerm, perms)

# Solution 2
# O(n * n!) Time | O(n * n!) Space
# Time: we have n! permutations, n calls for the helper method and eash helper call has n time of operation (Copy arr, delete arr element)
# Space: we have n! permutations with n length each.
def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]


def getPermutations(array):
    perm = []
    perms = []
    getPermutationsHelper(0, array, perms, len(array))
    return perms


def getPermutationsHelper(i, arr, perms, n):
	if i == n - 1:
		perms.append(arr[:])
	else:
		for j in range(i, n):
			swap(arr, i, j)
			getPermutationsHelper(i + 1, arr, perms, n)
			swap(arr, i, j)


array = [1, 2, 3]
result = getPermutations(array)
print(result)
