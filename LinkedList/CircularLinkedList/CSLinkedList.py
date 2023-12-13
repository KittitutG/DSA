class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self,):
        self.head = None
        self.tail = None
        self.length  = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if (temp_node == self.head):
                break
            result += '-->'
        return result
        

    # def __init__(self,value) :
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length  = 1

    def append(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length +=1

    

my_cslinkedlist = CSLinkedList()
my_cslinkedlist.append(10)
my_cslinkedlist.append(20)
my_cslinkedlist.append(30)


print(my_cslinkedlist)