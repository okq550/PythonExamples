class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

rootNode = TreeNode('Root')
leftNode = TreeNode('Left')
rightNode = TreeNode('Right')

rootNode.left = leftNode
rootNode.right = rightNode

# inOrderTraversal of the tree (Left, Root, Right)
def inOrderTraversal(root):
    visitedNodesValues = []
    
    if not root:
        return
    
    def df(node: TreeNode):
        if not node:
            return
        #Go lefts
        df(node.left)
        #Print the values
        visitedNodesValues.append(node.value)
        #Then go rights
        df(node.right)
    
    df(root)
    return visitedNodesValues

# preOrderTraversal of the tree (Root, Left, Right)
def preOrderTraversal(root):
    visitedNodesValues = []
    
    if not root:
        return
    
    def df(node: TreeNode):
        if not node:
            return
        #Print the value
        visitedNodesValues.append(node.value)
        #Go lefts
        df(node.left)
        #Go rights
        df(node.right)
        
    df(root)
    return visitedNodesValues

# postOrderTraversal of the tree (Left, Right, Root)
def postOrderTraversal(root):
    visitedNodesValues = []
    
    if not root:
        return
    
    def df(node: TreeNode):
        if not node:
            return
        #Go lefts
        df(node.left)
        #Go rights
        df(node.right)
        #Print values
        visitedNodesValues.append(node.value)
        
    df(root)
    return visitedNodesValues

print(inOrderTraversal(rootNode))
print(preOrderTraversal(rootNode))
print(postOrderTraversal(rootNode))