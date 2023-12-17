class Node:
    def __init__(self,value) :
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def append(self,value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            
            cursor = self.tail
            cursor.next = new_node
            self.tail = new_node
        self.length +=1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
    
        # if node to be removed is the head node
        elif index == 0:
            popped_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node
    
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
    
            popped_node = temp.next

            # if node to be removed is the tail node
            if popped_node.next is None:
                self.tail = temp
    
            temp.next = temp.next.next
            popped_node.next = None
            self.length -= 1
            return popped_node
    def reverse(self):
        '''
        https://www.youtube.com/watch?v=TSDl7sRxWdU for better udnerstanding
        '''
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def find_middle(self):
        '''
        turtoise and hare.
        one pointer move twice faster at a time
        meanwhile other move one point at a time.
        this mean when fast finished the line
        pointer will be in the middle

        this will erase the ease of counting iteration before looping
        '''
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node