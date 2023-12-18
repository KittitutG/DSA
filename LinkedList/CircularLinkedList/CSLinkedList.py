class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

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

    def search(self,target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False
    
    def get(self,index):
        if index ==-1:
            return self.tail

        elif index <-1 or index >= self.length-1:
            raise 'Out of boubd index'
        
        elif index == 0:
            return self.head
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        poped_node = self.head
        if self.length ==0:
            return None
        if self.length ==1:
            self.head = self.tail = None
        else:       
            self.head = self.head.next
            self.tail.next = self.head
            poped_node.next = None
        self.length -=1
        return poped_node
    
    def pop(self):
        if self.length ==0:
            return None
        poped_node = self.tail
        if self.length ==1:
            self.head = self.tail = None
        else:
            current_node = self.head
            while current_node.next is not self.tail:
                current_node = current_node.next
            current_node.next = self.head
            self.tail = current_node
            poped_node.next = None
        self.length -=1
        return poped_node

    def remove(self,index):
        if index <0 or index>= self.length:
            return None
        if index ==0:
            return self.pop_first()
        if index ==self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        poped_node = prev_node.next
        prev_node.next = poped_node.next
        poped_node.next = None
        self.length -=1
        return poped_node

    def delete_all(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = self.tail = None
        self.length = 0



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
# my_cslinkedlist.traverse()
# print(my_cslinkedlist.search(10))
print(my_cslinkedlist.remove(7))
my_cslinkedlist.delete_all()
my_cslinkedlist.delete_all()

print(my_cslinkedlist)
