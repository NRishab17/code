#code for DoubleEndedqueue
class DEqueue:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def addrear(self,data):
        self.items.append(data)
    def addfront(self,data):
        self.items.insert(0,data)
    def removefront(self):
         return self.items.pop(0)
    def removerear(self):
        return  self.items.pop()
'''a=DEqueue()
print(a.isempty())
a.addrear(8)
a.addrear(9)
a.addfront(7)
a.addfront(6)
print(a.items)
print(a.removefront())
print(a.removerear())
print(a.items)'''
#code for queue
from collections import deque
class queue:
    def __init__(self):
        self.buffer=deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)
    def front(self):
        return self.buffer[-1]
#placing orders using queue
a=queue()
def placeorder(key):
    for i in key:
        a.enqueue(i)
'''b=['pizza','burger']
placeorder(b)
print(a.dequeue())
print(a.dequeue())'''
#making pattern using queue
def producebinary(n):
    number=queue()
    number.enqueue('1')
    for i in range(n):
        front=number.front()
        print(front)
        number.enqueue(front+'0')
        number.enqueue(front+'1')
        number.dequeue()        
#producebinary(9)






        
    
        
        
        
        