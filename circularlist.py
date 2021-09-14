#creating circularlist and functions
class Node:
    def __init__(self,data=None,next=None):
        self.data=data 
        self.next=None
        
class circularlist:
    def __init__(self):
        self.head=None
  
    def append(self,data):
        if not self.head:
            self.head=Node(data)
            self.head.next=self.head
        else: 
            newnode=Node(data)
            cur=self.head
            while cur.next!=self.head:
                cur=cur.next 
            cur.next=newnode 
            newnode.next=self.head
    def printelements(self):
        cur=self.head
        while cur:
            print(cur.data,end=' ')
            cur=cur.next 
            if cur==self.head:
                break
    def prepend(self,data):
        newnode=Node(data)
        cur=self.head
        newnode.next=self.head
        if not self.head:
            newnode.next=newnode
        else:
            while cur.next!=self.head:
                cur=cur.next 
            cur.next=newnode 
        self.head=newnode
    def remove(self,key):
        if self.head.data==key:
            cur=self.head
            while cur.next!=self.head:
                cur=cur.next 
            cur.next=self.head.next 
            self.head=self.head.next 
        if self.head==self.head.next and self.head.data==key:
            self.head=None
        else:
            cur=self.head
            prev=None
            while cur.next!=self.head:
                prev=cur 
                cur=cur.next 
                if cur.data==key:
                    prev.next=cur.next 
                    cur=cur.next 
                    
#queue for circularlist
class circlequeue:
    def __init__(self,size):
        self.size=size
        self.front=-1
        self.rear=-1
        self.queue=[None for i in range(size)]
    def enqueue(self,data):
        if ((self.rear+1)%self.size==self.front):
            print('queue is full')
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if self.front==-1:
            print('empty queue')
        elif self.front==self.rear:
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp 
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
'''a=circularlist()
a.append(12)
a.append(13)
a.printelements()
a.remove(12)
print('remove12')
a.printelements()
a.prepend(10)
a.printelements()
a=circlequeue(5)
a.enqueue(10)
a.enqueue(11)
a.enqueue(12)
print(a.dequeue())'''
