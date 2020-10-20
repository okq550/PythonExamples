class Stack:
    def __init__(self, initalVal=[]):
        self.stack = initalVal
        
    def push(self, item):
        self.stack.append(item)
        return self.stack
    
    def pop(self):
        #Pop items from behind.
        return self.stack.pop(-1)
        
    def printStack(self):
        print(self.stack)
        
    def peak(self):
        return self.stack[-1]
    
    
myStack = Stack([0, 1 ,2])
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.printStack()
myStack.pop()
myStack.pop()
myStack.printStack()