class Node():
    def __init__(self,value,next):
        self.value = value
        self.next = next
    
    def __str__(self) -> str:
        string = str(self.value)
        while self.next:
            string += ','+str(self.next)
        return string
    
class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        return None if not self.minNode else self.minNode.value
    
    def push(self,item):
        if  self.minNode and (self.minNode.value < item):
            self.minNode = Node(value=self.minNode.value,next=self.minNode)
        else:
            self.minNode = Node(value=item,next=self.minNode)
        self.top = Node(value=item,next=self.top)

    def pop(self):
        if not self.top:
            return False
        else:
            self.minNode = self.minNode.next
            value = self.top.value
            self.top = self.top.next
            return value
        
cusStack = Stack()
cusStack.push(5)
print(cusStack.min())
cusStack.push(6)
print(cusStack.min())
cusStack.push(3)
print(cusStack.min())
cusStack.pop()
print(cusStack.min())

