class Queue:
    def __init__(self, initalVal=[]):
        self.queue = initalVal
        
    def enQueue(self, item):
        self.queue.append(item)
    
    def deQueue(self):
        #Pop items from the head
        self.queue.pop(0)
        
    def printQueue(self):
        print(self.queue)


myQueue = Queue([0])
myQueue.enQueue(1)
myQueue.enQueue(2)
myQueue.enQueue(3)
myQueue.printQueue()
myQueue.deQueue()
myQueue.printQueue()
myQueue.deQueue()
myQueue.printQueue()