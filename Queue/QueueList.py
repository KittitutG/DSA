class Queue():
    def __init__(self):
        self.list = []

    def __str__(self) -> str:
        value = [str(x) for x in self.list]
        return ' '.join(value)
    
    def isEmpty(self):
        return True if self.list == [] else False
    
    def enqueue(self,value):
        return self.list.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            return 'Empty queue'
        return self.list.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return 'Empty queue'
        return self.list[0]
    
    def deleteQueue(self):
        self.list = []
    
customQueue = Queue()
customQueue.enqueue(0)
customQueue.enqueue(1)            
customQueue.enqueue(2)
print(customQueue)   
customQueue.dequeue()
print(customQueue)
                    