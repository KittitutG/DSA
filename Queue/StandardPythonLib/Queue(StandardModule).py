'''
standard lib from python
'''
import queue as q
cq = q.Queue(maxsize=3)
print(cq.empty())
cq.put(1)
cq.put(2)
cq.put(3)
print(cq.full())
print(cq.get())
print(cq.qsize())
