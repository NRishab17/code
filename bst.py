#code for binarysearchtree
class bst:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def addchild(self,data):
        if data==self.data:
            return 
        elif data<self.data:
            if self.left:
                self.left.addchild(data)
            else:
                self.left=bst(data)
        else:
            if self.right:
                self.right.addchild(data)
            else:
                self.right=bst(data)
    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def mintree(self):
        if self.left is None:
            return self.data
        return self.left.mintree()
    
    def maxtree(self):
        if self.right is None:
            return self.data
        return self.right.maxtree()
    
    
    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right 
            if self.right is None:
                return self.left 
            minval=self.right.mintree()
            self.data=minval
            self.right=self.right.delete(minval)
        return self
    def inorder(self): #returns list in asceding order
        elements=[]
        if self.left:
            elements+=self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorder()
        return elements
    def preorder(self):
        elements=[self.data]
        if self.left:
            elements+=self.left.preorder()
        if self.right:
            elements+=self.right.preorder()
        return elements
    def postorder(self):
        elements=[]
        if self.left:
            elements+=self.left.postorder()
        if self.right:
            elements+=self.right.postorder()
        elements.append(self.data)
        return elements
    def sumoftree(self):
        leftsum=self.left.sumoftree() if self.left else 0
        rightsum=self.right.sumoftree() if self.right else 0
        return self.data+leftsum+rightsum
'''root=bst(17)
root.addchild(4)
root.addchild(23)                         17
root.addchild(6)                         /  \
root.addchild(7)                       6     18
root.addchild(18)                     /  \   / \
root.addchild(25)                    4   7  23  25
print(root.mintree())
print(root.maxtree())               
print(root.sumoftree())               
print(root.inorder())             
print(root.preorder())           
print(root.postorder())
print(root.delete(7))'''
#code for binarytree
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val,end=' ')
        if self.right:
            self.right.inorder()            
    def postorder(self):                     
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.val,end=' ')
    def preorder(self):
        print(self.val,end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()  
'''root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)           1
root.preorder()                 /\
print()                        2  3
root.postorder()              /
print()                      4
root.inorder()
print()'''
  
    