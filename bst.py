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
'''we try to print elements of tree when viewed from rightside
eg:  a)  1          b)   1
        / \           / \ 
        2  3         2   3
        /            / \ 
        4           4  5
a)1 3 4 are visisble from right side so these areprinted
b)1 3 5 are visisble from side as 4 is hided by 5 on viewing from right side
we declare maxlevel to keep maxlevel for each recursion(as a list)

rot is none is base case Whenever we see a node whose level is more than maximum level so far, we print the node because this is the last node in its level
we call right side of subtree first in recursion then left as right element can hide left element'''
class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
def rightViewUtil(root, level, max_level):
    if root is None:
        return
    if (max_level[0] < level):
        print (root.val)
        max_level[0] = level
    rightViewUtil(root.right, level+1, max_level)
    rightViewUtil(root.left, level+1, max_level)
def rightView(root):
    max_level = [0]
    rightViewUtil(root, 1, max_level)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.left.left=Node(4)
rightView(root)
def leftViewUtil(root, level, max_level):
    # Base Case
    if root is None:
        return
    # If this is the first node of its level
    if (max_level[0] < level):
        print(root.val)
        max_level[0] = level
    # Recur for left and right subtree
    leftViewUtil(root.left, level + 1, max_level)
    leftViewUtil(root.right, level + 1, max_level)
def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.left.left=Node(4)
leftView(root)
''' we print elements of tree when viewed from left side so left side elements hide right subtree if not rightsubtree is print 
as soon as 1st element is found of its level we print it and set new max level then itrerate through left tree first then right tree '''
def pathToNode(root, path, k): 
    # base case handling
    if root is None:
        return False
     # append the node value in path
    path.append(root.val)
    # See if the k is same as root's data
    if root.val== k :
        return True
    # Check if k is found in left or right
    # sub-tree
    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right!= None and pathToNode(root.right, path, k))):
        return True
    # If not present in subtree rooted with root,
    # remove root from path and return False
    path.pop()
    return False
def distance(root, data1, data2):
    if root:# store path corresponding to node: data1,data2
        path1 = []
        pathToNode(root, path1, data1)
        path2 = []
        pathToNode(root, path2, data2)
        # iterate through the paths to find the
        # common path length
        i=0
        while i<len(path1) and i<len(path2):
            # get out as soon as the path differs
            # or any path's length get exhausted
            if path1[i] != path2[i]:
                break
            i = i+1
         # get the path length by deducting the
        # intersecting path length (or till LowestCommonAncestor) 
        return (len(path1)+len(path2)-2*i)#we subtract 2*i as commonancestor is repeated in counting path of 2 points 
    else:
        return 0
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.left.left=Node(4)
print(distance(root, 3, 2))
'''       b)   1
              / \
             2   3
            / \ 
           4  5
we try to print shortest distance between given 2 points distance=no.of edges between 2 points 
eg: from 5 to 3 we go to 2,1,3 to reach three so distance is 3 and its shortest distance
The distance between two nodes can be obtained
Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca) 
we store path corresponding to give node and call pathtonode function
in pathtonode we try to find in which subtree node value our pathvalue=k value
then in distance function get out as soon as the path differor  or any path's length get exhausted
as soon as path1[i]!=path2[i] break the loop and return Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca) '''
# Function to convert binary tree into
# linked list by altering the right node
# and making left node point to None
def flatten(root):
    # Base condition- return if root is None
    # or if it is a leaf node
    if (root == None or root.left == None and
                        root.right == None):
        return
    # If root.left exists then we have
    # to make it root.right
    if (root.left != None):
        # Move left recursively
        flatten(root.left)
        # Store the node root.right
        tmpRight = root.right
        root.right = root.left
        root.left = None
        # Find the position to insert
        # the stored value  
        t = root.right
        while (t.right != None):
            t = t.right
        # Insert the stored value
        t.right = tmpRight
    # Now call the same function
    # for root.right
    flatten(root.right)
def inorder(root):#to print inorder way
    if (root == None):
        return
    inorder(root.left)
    print(root.val, end = ' ')
    inorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(5)
root.right.left=Node(4)
inorder(root)
flatten(root)
print()
inorder(root)
'''            1           1
              / \          \
             2   3          2
             / \              \             flatten version
            4  5               4
                               \
                                5
                                 \
                                 3
binary tree flatten in linked list(not using other ds) such that left node point to none and right points to next node
Base condition- return if root is None or if it is a leaf node
we covert all left subtree nodes to right side elements then right side elements get pushed down as left occupy those positions'''
def printkDistanceNodeDown(root, k):     
    # Base Case
    if root is None or k< 0 :
        return
    # If we reach a k distant node, print it
    if k == 0 :
        print (root.val)
        return
    # Recur for left and right subtree
    printkDistanceNodeDown(root.left, k-1)
    printkDistanceNodeDown(root.right, k-1)
# Prints all nodes at distance k from a given target node The k distant nodes may be upward or downward. This function
# returns distance of root from target node, it returns -1
# if target node is not present in tree rooted with root
def printkDistanceNode(root, target, k):
    # Base Case 1 : IF tree is empty return -1
    if root is None:
        return -1
    # If target is same as root. Use the downward function
    # to print all nodes at distance k in subtree rooted with
    # target or root
    if root == target:
        printkDistanceNodeDown(root, k)
        return 0
    # Recur for left subtree
    dl = printkDistanceNode(root.left, target, k)
    # Check if target node was found in left subtree
    if dl != -1:
        # If root is at distance k from target, print root
        # Note: dl is distance of root's left child
        # from target
        if dl +1 == k :
            print (root.val)
        # Else go to right subtreee and print all k-dl-2
        # distant nodes
        # Note: that the right child is 2 edges away from
        # left chlid
        else:
            printkDistanceNodeDown(root.right, k-dl-2)
        # Add 1 to the distance and return value for
        # for parent calls
        return 1 + dl
    # MIRROR OF ABOVE CODE FOR RIGHT SUBTREE
    # Note that we reach here only when node was not found
    # in left subtree
    dr = printkDistanceNode(root.right, target, k)
    if dr != -1:
        if (dr+1 == k):
            print (root.val)
        else:
            printkDistanceNodeDown(root.left, k-dr-2)
        return 1 + dr
    # If target was neither present in left nor in right subtree
    return -1
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
printkDistanceNode(root,root.left.right, 2)
'''we print all node k given distance from target node
There are two types of nodes to be considered. 
1) Nodes in the subtree rooted with target node. For example, if the target node is 8 and k is 2, then such nodes are 10 and 14. 
2) Other nodes, may be an ancestor of target, or a node in some other subtree. For target node 8 and k is 2, the node 22 comes in this category.
Finding the first type of nodes is easy to implement. Just traverse subtrees rooted with the target node and decrement k in recursive call. When the k becomes 0, print the node currently being traversed (See this for more details). Here we call the function as printkdistanceNodeDown().
How to find nodes of second type? For the output nodes not lying in the subtree with the target node as the root, we must go through all ancestors. For every ancestor, we find its distance from target node, let the distance be d, now we go to other subtree (if target was found in left subtree, then we go to right subtree and vice versa) of the ancestor and find all nodes at k-d distance from the ancestor.'''
