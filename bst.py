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
def printkthlevelsum(root,k):
        if root==None:
            return 0
        q=[]
        q.append(root)
        level=0
        sum=0
        flag=0
        while len(q)!=0:
            size=len(q)
            while size!=0:
                size-=1
                ptr=q[0]
                q.pop(0)
                if level==k:
                    sum+=ptr.val
                    flag=1
                else:
                    if ptr.left:
                        q.append(ptr.left)
                    if ptr.right:
                        q.append(ptr.right)
            level+=1
            if flag==1:
                break 
        return sum            
def printlevelorder(root):
    h=height(root)
    for i in range(1,h+1):
        printcurrentlevel(root,i)
def printcurrentlevel(root,level):
    if root is None:
        return
    if level==1:
        print(root.val,end=' ')
    elif level>1:
        printcurrentlevel(root.left, level-1)
        printcurrentlevel(root.right, level-1)
def height(root):#returns length of tree
    if root is None:#no root element so return 0
        return 0
    else:
        lheight=height(root.left)
        rheight=height(root.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1
#diameter of tree is no of nodes on longest path between 2 end nodes in our case from 4-3
#diameter=max(diameter of left subtree or right subtree or longest path between leaves through root(which is height of subtrees of root))
#when 5 was added diameter became 4 as 5-4-2-1 is longer
def diameter(root):
    if root is None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    lwidth=diameter(root.left)
    rwidth=diameter(root.right)
    return max(lheight+rheight+1,(max(rwidth,lwidth)))
'''we add values of child nodes to parent such that parent node=parentnode value+child values root is found to be sum of all nodes ofbinary tree'''
def sumreplacement(root):
    if root==None:
        return
    sumreplacement(root.left)
    sumreplacement(root.right)
    if root.left:
        root.val+=root.left.val
    if root.right:
        root.val+=root.right.val
''' mod(left subtree height - right subtree height)<=1 is a balanced height tree'''
'''      a)        1         b)       1
                 /\                / \
                2  3              2   3
             /                  /
            4                   4
                                \                 
                                5
in a) 4 is child so is balanced,2 has left subtree only abs(lh-rh)=1, 3 is child node so balanced,1 has 2 subtree lh=2 and rh=1 so abs(lh-rh)=1
in b) 5 is child so balanced,4 has right subtree so abs(lh-rh)=abs(0-1)=1,2 has left subtree so abs(lh-rh)=abs(2-0)=2 so unbalanced'''
                                       
def balancedheighttree(root):
    if root==None:
        return True
    if balancedheighttree(root.left)==False:
        return False
    if balancedheighttree(root.right)==False:
        return False
    lh=height(root.left)
    rh=height(root.right)
    if abs(lh-rh)<=1:
        return True
    else:
       return False
#root=Node(1)
#root.left=Node(2)
#root.right=Node(3)
#root.left.left=Node(4) 
#root.left.left.right=Node(5)     1                1
#root.preorder()                 /\                / \
#print()                        2  3              2   3
#root.postorder()              /                  /
#print()                      4                   4
#root.inorder()                                    \
#print()                                            5
