from random import randint

class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return self.value

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

    def __str__(self) -> str:
        result = [str(x.value) for x in self]
        return '-->'.join(result)
    
    def __len__(self):
        count = 0
        tempNode = self.head
        while tempNode:
            count +=1
            tempNode =tempNode.next
        return count
    
    def add(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            
            self.tail.next = new_node
            self.tail = new_node
        return self
    
    def generate(self,n,min_val,max_val):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_val,max_val))
        return self
    
    def remove_duplicate(self):
        '''
        This function works by checking each node in the LinkedList against all the subsequent nodes for duplicates. 
        If a duplicate is found, it's removed by updating the next attribute of the node before it, thus bypassing the duplicate node. 
        In the end, the tail of the LinkedList is updated to the last node in the list.
        '''
        current_node = self.head
        prev_node = None
        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            prev_node = current_node
            current_node = current_node.next
        self.tail =prev_node
        return self.head

          
    
# my_ll = LinkedList()
# my_ll.generate(5,1,4)
# print(my_ll)
# my_ll.remove_duplicate()
# print(my_ll)        
