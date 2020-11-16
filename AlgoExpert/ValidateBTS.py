# O(n) Time | O(d) Space where d is the depth of the tree.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(node, minVal, maxVal):
	if node is None:
		return True
	
	if node.value < minVal or node.value >= maxVal:
		return False
	
	validateLeftSubTree = validateBstHelper(node.left, minVal, node.value)
	
	return validateLeftSubTree and validateBstHelper(node.right, node.value, maxVal)


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

result = validateBst(root)

print(result)