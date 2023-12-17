'''
Node: this is data element on Linked List
we need an individual class for Node becase when we considering a class properties
#1 Node should not know their neightbour
#2 Every Node is unique on theri own (chagning one node would not affect others)

Node also have their own properties
#1 value
#2 pointer to other node
'''

class Node:
    '''
    
    constructor
    time conplexity: O(1)
    space conplexity: O(1)
   
    '''
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    '''
    
    constructor
    time conplexity: O(1)
    space conplexity: O(1)
   
    '''
    # def __init__(self,value):
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     self.lenth = 1

    def __init__(self):
        self.head = None
        self.tail = None
        self.lenth = 0

    def __str__(self):
        temp_node = self.head
        string_result = ''
        while temp_node is not None:
            string_result += str(temp_node.value)
            if temp_node.next is not None:
                string_result +=' --> '
            temp_node = temp_node.next
        return string_result

    def  append(self,value):
        '''
        time conplexity: O(1)
        space conplexity: O(1)
        '''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenth +=1

    def prepend(self,value):
        '''
        time conplexity: O(1)
        space conplexity: O(1)
        '''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.lenth +=1

    def insert(self,value,index):
        '''
        time conplexity: O(N)
        space conplexity: O(1)
        '''
        new_node = Node(value)
        temp_node = self.head
        if index < 0 or index > self.lenth:
            return False
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.lenth +=1
        return True

    def traverse(self):
        '''
        time conplexity: O(N)
        space conplexity: O(1)
        '''
        current = self.head
        while current:
            print(current.value)
            current = current.next 

    def search(self,target):
        '''
        time conplexity: O(N)
        space conplexity: O(1)
        '''
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index +=1
        return -1                

    def get(self,index):
        '''
        time conplexity: O(N)
        space conplexity: O(1)
        '''
        current = self.head
        if index ==-1:
            return self.tail
        if index < -1 or index >= self.lenth:
            return False
        for _ in range(index):
            current = current.next
        return current

    def set_value(self,index,value):
        '''
        time conplexity: O(N) --> chain from get() method
        space conplexity: O(1)
        '''
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        '''
        time conplexity: O(1) 
        space conplexity: O(1)
        '''
        poped_node = self.head
        if self.lenth ==0:
            return False
        if self.lenth == 1:
            self.head = None
            self.tail =None
        else:
            self.head = self.head.next
            poped_node.next = None
        self.lenth -=1
        return poped_node

    def pop(self):
        '''
        time conplexity: O(1) 
        space conplexity: O(1)
        '''
        poped_node = self.tail
        current = self.head
        if self.lenth ==0:
            return False
        if self.lenth == 1:
            self.head = None
            self.tail =None
        else:
            while current.next is not self.tail:
                current = current.next
            self.tail = current
            current.next = None       
        self.lenth -=1
        return poped_node.value

    def remove(self,index):
        '''
        time conplexity: O(N) --> chain from get(),pop()
        space conplexity: O(1)
        '''
        if index >= self.lenth or index <-1:
            return False
        elif index ==0:
            return self.pop_first()
        elif self.lenth == index-1 or index ==-1:
            return self.pop()
        prev_node = self.get(index-1)
        poped_node = prev_node.next
        prev_node.next = poped_node.next
        poped_node.next = None
        self.lenth -=1
        return poped_node

    def delete_all(self):
        '''
        time conplexity: O(1) 
        space conplexity: O(1)
        '''
        self.head = None
        self.tail = None
        self.lenth =0

    def deleteDuplicates(self):
        cursor = self.head
        while cursor and cursor.next:
          
            if cursor.value == cursor.next.value:
                cursor.next = cursor.next.next

            else:
                cursor = cursor.next


my_link = LinkedList()
my_link.append(1)
my_link.append(2)
my_link.append(2)
my_link.append(3)
my_link.append(3)
my_link.append(3)
print(my_link)

my_link.deleteDuplicates()
print(my_link)