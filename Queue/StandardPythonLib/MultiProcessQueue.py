from multiprocessing import Queue
'''
Multiprocess across thread
'''
cq = Queue(maxsize=3)
cq.put(1)
print(cq.get(1))