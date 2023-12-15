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


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node  
        self.length += 1

    def insert(self,value,index):
        new_node = Node(value)
        if index <0 or index > self.length:
            raise Exception('Index out of bound')
           
        if index ==0:
            if self.length ==0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node

            self.prepend(value)

        if index ==self.length:
            self.append(value)
        else:   
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1

    def traverse (self):
        temp_node = self.head
        if self.length ==0:
            return False
        else:
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.head:
                    break

my_cslinkedlist = CSLinkedList()

my_cslinkedlist.prepend(10)
my_cslinkedlist.append(10)
my_cslinkedlist.prepend(20)
my_cslinkedlist.append(30)
my_cslinkedlist.insert(30,0)
my_cslinkedlist.insert(70,6)
# my_cslinkedlist.insert(70,10)

print(my_cslinkedlist)
# print(my_cslinkedlist.tail.value)
my_cslinkedlist.traverse()