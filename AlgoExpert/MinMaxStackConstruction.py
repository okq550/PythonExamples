# Solution 1:
class MinMaxStack:
	def __init__(self):
	    """This is the constructor for class

        Returns:
            [type]: [description]
        """
		self.minMaxStack = []
		self.stack = []
    
    # O(1) Time | O(1) Space
    def peek(self):
        return self.stack[-1]

	# O(1) Time | O(1) Space
    def pop(self):
        # ! This is to get the last item in the stack.
        # ? Where do go from here?
        # # Important note!
        # TODO: We need to add some logging here.
        # @param myParam is the.
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
