class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail    = None
    
    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

class Queue():
    def __init__(self) -> None:
        self.linkedList = LinkedList()

    def __str__(self) -> str:
        value = [str(x.value) for x in self.linkedList]
        return '-->'.join(value)
    
    def isEmpty(self):
        return True if self.linkedList.head is None else False
    
    def enqueue(self,value):
        new_node = Node(value)
        if not self.linkedList.head:
            self.linkedList.head = new_node
            self.linkedList.tail = new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            return "Empty"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next

        return tempNode
    
    def peek(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.linkedList.head
        
    def deleteQueue(self):
        self.linkedList.tail = self.linkedList.head = None
        

# customQueue = Queue()
# customQueue.enqueue(0)
# customQueue.enqueue(1)            
# customQueue.enqueue(2)
# print(customQueue)   
# print(customQueue.dequeue())
# print(customQueue.peek())
# customQueue.deleteQueue()                    