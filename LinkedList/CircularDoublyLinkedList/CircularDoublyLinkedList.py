class Node():
    def __init__(self,value) :
        self.value = value
        self.next = None
        self.prev = None

    
class DoublyLinkedList():
    def    __init__(self):
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

my_cdll = DoublyLinkedList()
my_cdll.create(20)
print([i.value for i in my_cdll])
