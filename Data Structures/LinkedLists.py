class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

headNode = ListNode(1)
secondNode = ListNode(2)
thirdNode = ListNode(3)

headNode.next = secondNode
secondNode.next = thirdNode

# #Traversing the linked list
currentNode = headNode
while currentNode is not None:
    print(currentNode.val)
    currentNode = currentNode.next

# insert new listnode with value of 5 in between the secondNode and thirdNode
currentNode = headNode
while currentNode.val != 2:
    currentNode = currentNode.next

newNode = ListNode(5)
newNode.next = currentNode.next
currentNode.next = newNode