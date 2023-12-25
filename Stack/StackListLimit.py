# create
# push
# pop
# peek
# isEmpty
# isFull
# deketeStack

'''
Stack with python list(no size limit)
'''
class Stack:
    def __init__(self,maxSize) :
        self.maxSize = maxSize
        self.list = []

    def __str__(self) -> str:
        element = reversed(self.list)
        element = [str(i) for i in element]
        return '\n'.join(element)
    
        
    def isEmpty(self):
        return True if self.list == [] else False
    
    def isFull(self):
        return True if len(self.list) == self.maxSize else False
    
    def push(self,value):
        if self.isFull():
            return 'Fully allocated'
        else:
            self.list.append(value)
            return 'Inserted Successfully'
        
    def pop(self):
        if self.isEmpty():
            return 'Empty'
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return 'This is Empty'
        else:
            return self.list[len(self.list)-1]
     
    def deleteStack(self):
        self.lis == None

customStack = Stack(4)
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack)
print('-----------')
