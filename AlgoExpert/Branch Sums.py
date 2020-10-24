# O(n) Time | O(n) Space
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSumsHelper(node, totalSum, branchSums):
	if node is None:
		return
	
	totalSum += node.value
	
	if node.left is None and node.right is None:
		branchSums.append(totalSum)
		return branchSums
	
	if node.left is not None:
		branchSumsHelper(node.left, totalSum, branchSums)
	
	if node.right is not None:
		branchSumsHelper(node.right, totalSum, branchSums)
  
def branchSums(root):
    if not root:
        return
    branchSums = []
    branchSumsHelper(root, 0, branchSums)
    return branchSums