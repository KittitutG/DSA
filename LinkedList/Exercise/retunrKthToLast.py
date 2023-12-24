from LinkedList import LinkedList


def nthToLast(ll,n):
    pointer1 = ll.head
    pointer2 = ll.head
    for _ in range(n):
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1.value

my_ll = LinkedList()
my_ll.generate(10,0,20)
print(my_ll)
print(nthToLast(my_ll,10))
