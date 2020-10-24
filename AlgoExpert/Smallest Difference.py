# Solution 1
# O(n * m) Time | O(1) Space

# def distance(x, y):
# 	x = int(x)
# 	y = int(y)
# 	return abs(x - y)

# def smallestDifference(arrayOne, arrayTwo):
#     arrayOne.sort()
# 	arrayTwo.sort()

# 	closesPairsArray = [float("inf"), float("inf")]
# 	closestDiff = float("inf")

# 	for i in range(len(arrayOne)):
# 		left = 0
# 		right = len(arrayTwo) - 1

# 		while left < right:
# 			distance1 = distance(arrayOne[i], arrayTwo[left])
# 			distance2 = distance(arrayOne[i], arrayTwo[right])

# 			if distance1 <= distance2 and distance1 < closestDiff:
# 				closesPairsArray = [arrayOne[i], arrayTwo[left]]
# 				right -= 1
# 			elif distance2 <= distance1 and distance2< closestDiff:
# 				closesPairsArray = [arrayOne[i], arrayTwo[right]]
# 				left += 1
# 			else:
# 				left += 1
# 				right -= 1
# 	# print(closesPairsArray)
# 	return closesPairsArray