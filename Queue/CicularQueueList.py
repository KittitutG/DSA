class Queue():

    '''
    Circular queue will reduce time complexity for enqueue/dequeue from standard QueueList by adding pointer(start/top)
    '''
    def __init__(self,size) -> None:
        self.list = size * [None]
        self.size = size
        self.start = -1
        self.top = -1
    
    def __str__(self) -> str:
        values = [str(x) for x in self.list]
        return ' '.join(values)
    
    def isFull(self):
        if self.top+1 == self.start:
            return True
        elif self.start ==0 and self.top+1 ==self.size:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top ==-1:
            return True
        else:
            return False
        
    def enqueue(self,value):
        if self.isFull():
            return "Full"
        else:
            if self.top +1 == self.size:
                self.top =0
            else:
                self.top +=1
                if self.start ==-1:
                    self.start = 0
            self.list[self.top] = value
        return "Inserted Successfully"
    
    def dequeue(self):
        if self.isEmpty():
            return "Empty"
        else:
            startElement = self.list[self.start]
            start = self.start
            if self.start == self.top:
                self.start =-1
                self.top =-1
            elif self.start +1 == self.size:
                self.start =0
            else:
                self.start +=1
            self.list[start] = None
        return startElement
    
    def peek(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.list[self.start]
        
    def deleteQueue(self):
        self.size = self.size*[None]
        self.start = self.top = -1
    
        
        
customQueue = Queue(3)
print(customQueue.isFull())
customQueue.enqueue(0)
customQueue.enqueue(1)            
customQueue.enqueue(2)
print(customQueue)   
customQueue.dequeue()
print(customQueue)
