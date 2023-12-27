class MultiStack:
    def __init__(self,stacksize) -> None:
        self.numberstacks = 3
        self.custList = [0] * (stacksize* self.numberstacks)
        self.size = [0]*self.numberstacks
        self.stacksize = stacksize

    def isFull(self,stacknumber):
        return True if self.size[stacknumber] == self.stacksize else False
    
    def isEmpty(self,stacknumber):
        return True if self.size[stacknumber] ==0 else False
    
    def indexOfTop(self,stacknum):
        offset = stacknum * self.stacksize
        return offset + self.size[stacknum] -1
    
    def push(self,value,stacknumber):
        if self.isFull(stacknumber):
            return "this is Full"
        else:
            self.size[stacknumber] += 1
            self.custList[self.indexOfTop(stacknumber)] = value 

    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            return "This is Empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.size[stacknum] -=1
            return value      
        
    def peek(self,stacknum):
        if self.isEmpty(stacknum):
            return "This is Empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            return value      

myStack = MultiStack(6)
print(myStack.isFull(0))
print(myStack.isEmpty(2))
myStack.push(1,0)
myStack.push(2,0)
myStack.push(1,1)
print(myStack.peek(0))