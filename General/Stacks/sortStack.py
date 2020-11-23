# Solution 1:
class MinMaxStack:

    def __init__(self):
        self.minMaxStack = []
        self.stack = []
        
    def print(self):
        print(self.stack)

    # O(1) Time | O(1) Space
    def peek(self):
        return self.stack[-1]

    # O(1) Time | O(1) Space
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop(-1)

    # O(1) Time | O(1) Space
    def push(self, number):
        newMinMax = {'min': number, 'max': number}
        if len(self.stack):
            lastMinMax = self.minMaxStack[-1]
            newMinMax['min']: min(lastMinMax['min'], number)
            newMinMax['max']: max(lastMinMax['max'], number)

        self.stack.append(number)
        self.minMaxStack.append(newMinMax)

    # O(1) Time | O(1) Space
    def getMin(self):
        return min(self.stack)

    # O(1) Time | O(1) Space
    def getMax(self):
        return max(self.stack)
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def sortedInsert(self, x):
        if self.isEmpty() or x > self.peek():
            self.push(x)
        
        temp = self.pop()
        self.sortedInsert(x)
        self.push(temp)
    
    def sort(self):
        if self.isEmpty():
            x = self.pop()
            self.sort()
            self.sortedInsert(x)

stack = MinMaxStack()
stack.push(5)
stack.push(7)
stack.push(2)
stack.print()
stack.sort()
