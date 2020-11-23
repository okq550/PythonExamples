# def get_cheapest_cost(rootNode):
#     branch_costs = []
#     traverseTree(rootNode, 0, branch_costs)
#     return min(branch_costs)

# def traverseTree(node, total_cost = 0, branch_costs = []):
    
#     total_cost += node.cost
    
#     if len(node.children) == 0:
#         branch_costs.append(total_cost)
#         return
    
#     for child in node.children:
#         traverseTree(child, total_cost, branch_costs)


MAX_INT = float('inf')

def get_cheapest_cost(rootNode):
    n = len(rootNode.children)
    
    if n == 0:
        return rootNode.cost
    else:
        min_cost = MAX_INT
        
        print(min_cost)
        
        for i in range(len(rootNode.children)):
              temp_cost = get_cheapest_cost(rootNode.children[i])
              if temp_cost < MAX_INT:
                  min_cost = temp_cost
        
        return min_cost + rootNode.cost

##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node
class Node:

    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None


# Root Childs
rootNode = Node(0)
rootNode.children = [Node(5), Node(3), Node(6)]

# 1st Root Child
rootNode.children[0].children = [Node(4)]

# 2nd Root Child
rootNode.children[1].children = [Node(2),Node(0)]
rootNode.children[1].children[0].children = [Node(1)]
rootNode.children[1].children[0].children[0].children = [Node(1)]
rootNode.children[1].children[1].children = [Node(10)]

# 3rd Root Child
rootNode.children[2].children = [Node(1), Node(5)]

print(get_cheapest_cost(rootNode))