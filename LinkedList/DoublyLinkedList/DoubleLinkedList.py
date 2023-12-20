class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
class DoublyLinkedList():
    def    __init__(self):
        self.head = self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result +='<->'
            temp_node = temp_node.next
        return result

    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        
    def prepend(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1

    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next

    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def search(self,target):
        temp_node = self.head
        index = 0
        while temp_node:
            if temp_node.value == target:
                return index
            temp_node = temp_node.next
            index +=1
        return -1

    def get(self,index):
        if index < 0 or index >=self.length:
            return None
        elif index < self.length //2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length-1,index,-1):
                current_node = current_node.prev
        return current_node

    def set_value(self,index,value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def insert(self,index,value):
        if index <0 or index > self.length:
            raise 'Index Our of Bound'
            
        new_node = Node(value)

        if index ==0:
            self.prepend(value)
            return
        
        elif index == self.length:
            self.append(value)
            return

        temp_node = self.get(index-1)
        new_node.next =temp_node.next
        new_node.prev =temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length +=1
        
    def pop_first(self):
        if not self.head:
            return None
        poped_node = self.head
        if self.length==1:
            self.head = self.tail = None
        else:           
            self.head = self.head.next
            self.head.prev = None
            poped_node.next = None
        self.length -=1
        return poped_node

    def pop(self):
        if not self.head:
            return None
        
        poped_node = self.tail
        if self.length ==1:
            self.head = self.tail = None
        else:
            
            self.tail = self.tail.prev
            self.tail.next = None
            poped_node.prev = None
        self.length -=1
        return poped_node
        
    def remove(self,index):
        
        if index <0 or index >self.length:
            raise "Out of bound"
        if index ==0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        else:
            poped_node = self.get(index)
            poped_node.prev.next = poped_node.next
            poped_node.next.prev = poped_node.prev
            poped_node.next = poped_node.prev = None
        self.length -=1
        return poped_node


my_dll = DoublyLinkedList()
my_dll.append(10)
my_dll.append(20)
my_dll.prepend(00)
my_dll.traverse()
print(my_dll)
my_dll.reverse_traverse()
