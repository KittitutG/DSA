from LinkedList import LinkedList, Node

def intersection(ll1,ll2):
    if ll1.tail is not ll2.tail:
        return False
    
    len1 = len(ll1)
    len2 = len(ll2)

    shorter = ll1 if len1 < len2 else ll2
    longer = ll2 if len1 < len2 else ll1

    diff = len(longer)- len(shorter)

    longerHead = longer.head
    shorterHead = shorter.head

    for _ in range(diff):
        longerHead = longerHead.next

    while shorterHead is not longerHead:
        shorterHead = shorterHead.next
        longerHead = longerHead.next
        

    return longerHead
#helper: add intersect part
def additionalIntersect(ll1,ll2,value):
    tempNode = Node(value)
    ll1.tail.next = tempNode
    ll1.tail = tempNode
    ll2.tail.next = tempNode
    ll2.tail = tempNode







my_ll = LinkedList()
my_ll.generate(5,0,9)
my_ll2 = LinkedList()
my_ll2.generate(3,0,9)
additionalIntersect(my_ll,my_ll2,20)
additionalIntersect(my_ll,my_ll2,6)

print(my_ll)
print(my_ll2)

res = intersection(my_ll,my_ll2)
print(res.value)