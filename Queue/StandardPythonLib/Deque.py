'''
standard lib from python
'''

from collections  import deque
custQueue = deque(maxlen = 3)
print(custQueue)


custQueue.append(1)
custQueue.append(2)
custQueue.append(3)
print(custQueue)

'''
will be pop out the first element if exceed limit
'''
custQueue.append(4)
print(custQueue)


custQueue.popleft()
print(custQueue)


custQueue.clear()
print(custQueue)
