#tree structure code
class TreeNode():
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def getlevel(self):
        level=0
        p=self.parent 
        while p:
            level+=1
            p=p.parent 
        return level 
    def printtree(self):
        spaces=' '*self.getlevel()
        print(spaces+self.data)
        if self.children:
            for child in self.children:
                child.printtree()
    def addchild(self,child):
        child.parent=self
        self.children.append(child)
'''a=treenode('electronics')
laptop=treenode('laptop')
laptop.addchild(treenode('mac'))
laptop.addchild(treenode('hp'))
phone=treenode('phone')
phone.addchild(treenode('vivo'))
phone.addchild(treenode('oppo'))
a.addchild(laptop)
a.addchild(phone)
a.printtree()
print(laptop.getlevel())'''

