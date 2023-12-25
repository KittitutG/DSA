# create
# push
# pop
# peek
# isEmpty
# isFull
# deketeStack
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

        
class Stack():
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        result = [str(x.value) for x in self.LinkedList] 
        return '\n'.join(result)
    
    def isEmpty(self):
        return True if not self.LinkedList.head else False
    
    def push(self,value):
        tempNode = Node(value)
        tempNode.next= self.LinkedList.head
        self.LinkedList.head = tempNode

    def pop(self):
        if self.isEmpty():
            return "Empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.LinkedList.head.value
        
    def deleteStack(self):
        self.LinkedList.head = None
    
customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print(customStack.pop())
