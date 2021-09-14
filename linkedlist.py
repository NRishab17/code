#code for linked list and functions
class Node:
    def __init__(self,data=None,next=None):
        self.data=data 
        self.next=next
                
class linkedlist:
    def __init__(self):
        self.head=None
        
    def printelements(self):
        if self.head is None:
            print('empty list')
            return
        itr=self.head 
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
        
    def length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next 
        return count
    
    def insertatbegining(self,data):
        node=Node(data,self.head)
        self.head=node 
        
    def insertatend(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head 
        while itr.next:
            itr=itr.next 
        itr.next=Node(data,None)
        
    def insertat(self,index,data):
        if index<0 or index>self.length():
            raise Exception('invalid index')
        if index==0:
            self.insertatbegining(data)
            return
        count=0
        itr=self.head 
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next 
            count+=1
            
    def removeat(self,index):
        if index<0 or index>self.length():
            raise Exception('invalid index')
        if index==0:
            self.head=self.head.next 
            return
        count=0
        itr=self.head 
        while itr:
            if count==index-1:
                itr.next=itr.next.next 
                break
            itr=itr.next 
            count+=1
            
    def insertvalues(self,list):
        self.head=None
        for i in list:
            self.insertatend(i)
            
    def insert_after(self,data_after,data_insert):
        if self.head is None:
            return
        if self.head.data==data_after:
            self.head.next=Node(data_insert,self.head.next)
            return
        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_insert,itr.next)
                break
            itr=itr.next
            
    def remove_by(self,value):
        if self.head is None:
            return
        if self.head.data==value:
            self.head=self.head.next
            
        itr=self.head 
        while itr.next:
            if itr.next.data==value:
                itr.next=itr.next.next 
                break
            itr=itr.next 
                
#code for stack in linked list       
class stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True            
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head 
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            popnode=self.head 
            self.head=self.head.next 
            popnode.next=None
            return popnode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        itr=self.head 
        if self.isempty():
            print('stack empty')
        else:
            while itr!=None:
                print(itr.data,'-->',end=' ')
                itr=itr.next 
            return 
#queue in linkedlist
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def isempty(self):
        return self.front==None
    def enqueue(self,data):
        if self.rear==None:
            self.front=Node(data)
            self.rear=self.front 
        else:
            self.rear.next=Node(data)
            self.rear=self.rear.next 
    def dequeue(self):
        if self.front==None:
            return None
        else:
            val=self.front.data
            self.front=self.front.next 
            return val
        
'''ll=linkedlist()
ll.insertvalues(['banana','mango','grapes','orange'])
ll.printelements()
ll.insert_after('banana','apple')
ll.printelements()
ll.remove_by('apple')
ll.printelements()'''
'''a=stack()
print(a.isempty())
a.push(10)
a.push(11)
a.display()
print(a.pop())
print(a.peek())'''
'''b=queue()
b.isempty()
b.enqueue(10)
b.enqueue(11)
b.enqueue(12)
print('queue front:'+str(b.front.data))
print('queue rear:'+str(b.rear.data))
print(b.dequeue())
print(b.dequeue())'''

        
            
        