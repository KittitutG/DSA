from LinkedList import LinkedList

def sumList(ll1,ll2):
    n1 = ll1.head
    n2 = ll2.head
    carry = 0 
    new_ll = LinkedList()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
           result += n2.value
           n2 = n2.next 
        new_ll.add(int(result%10))
        carry = result // 10
    return new_ll


my_ll = LinkedList()
my_ll.generate(3,0,9)
print(my_ll)
my_ll2 = LinkedList()
my_ll2.generate(3,0,9)
print(my_ll2)
print(sumList(my_ll,my_ll2))