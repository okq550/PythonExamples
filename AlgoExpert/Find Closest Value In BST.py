# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
# Solution 1 - Recursion
# Average: O(log(n)) Time | O(log(n)) Space
# Worst: O(n) Time | O(n) Space
def findClosestValueInBst(tree, target):
	closestNode = []
	
	def walkingThrough(node: BST):
		if not node:
			return
		
		# print('################ START ################')
		diff = abs(target - node.value)
		# print('Node: ' + str(node.value) + ', Diff: ' + str(diff))
		
		if len(closestNode) == 0:
			closestNode.append(node.value)
		else:
			# print('if ' + str(diff) + ' < ' + str(closestNode[0]))
			if diff < abs(target - closestNode[0]):
				closestNode[0] = node.value
		
		# print('closestNode: ', end='') 
		# print(closestNode)
		# print('################ END ################')
		# print()
			
		walkingThrough(node.right)
		walkingThrough(node.left)
	
	walkingThrough(tree)
	print(closestNode[0])
	return closestNode[0]

# # Solution 2 - Recursion
# # Average: O(log(n)) Time | O(log(n)) Space
# # Worst: O(n) Time | O(n) Space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(node, target, closestValue):
	if node is None:
		return closestValue
	
	if abs(target - closestValue) > abs(target - node.value):
		closestValue = node.value
	
	if target > node.value:
		return findClosestValueInBstHelper(node.right, target, closestValue)
	elif target < node.value:
		return findClosestValueInBstHelper(node.left, target, closestValue)
	else:
		return closestValue

# # Solution 3 - While
# # Average: O(log(n)) Time | O(1) Space
# # Worst: O(n) Time | O(1) Space
# def findClosestValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree, target, float("inf"))

# def findClosestValueInBstHelper(node, target, closestValue):
	currentNode = node
	
	while currentNode is not None:
		if abs(target - closestValue) > abs(target - currentNode.value):
			closestValue = currentNode.value
		if target > currentNode.value:
			currentNode = currentNode.right
		elif target < currentNode.value:
			currentNode = currentNode.left
		else:
			break
	return closestValue