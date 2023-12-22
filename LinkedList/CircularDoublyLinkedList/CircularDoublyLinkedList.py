class Node():
    def __init__(self,value) :
        self.value = value
        self.next = None
        self.prev = None

    
class DoublyLinkedList():
    def __init__(self):
        self.head = self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break


    def create(self,value):
        new_node = Node(value)
        self.head = self.tail = new_node
        new_node.next = new_node.prev = new_node
        return "Create successfully"

    def insert(self,value,index):
        if not self.head:
            return "Object not exists"
        else:
            new_node = Node(value)
            if index ==0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev =new_node
                self.head = new_node
                self.tail.next = new_node
            elif index ==1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                tempNode = self.head
                ind = 0
                while ind < index-1:
                    tempNode = tempNode.next
                    ind +=1
                new_node.next =tempNode.next
                new_node.prev =tempNode
                new_node.next.prev = new_node
                tempNode.next = new_node
            return "Insertion Successfully"

    def traversal(self):
        if not self.head:
            return "This is empty"
        else:
            tempNode= self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode =tempNode.next

    def reverse_travesal(self):
        if not self.head:
            return "This is empty"
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def search(self,target):
        if not self.head:
            return "This is empty"
        else:
            tempNode = self.head
            while tempNode:
                
                if tempNode.value == target:
                    return True
                if tempNode == self.tail:
                    break
                tempNode =tempNode.next
                
            return "Element not found"

my_cdll = DoublyLinkedList()
my_cdll.create(20)
my_cdll.insert(0,0)
my_cdll.insert(1,1)
my_cdll.insert(2,2)

print([i.value for i in my_cdll])
my_cdll.traversal()
my_cdll.reverse_travesal()
print(my_cdll.search(9))