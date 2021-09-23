'''convert expression to infex,postfix,prefix eg:4*2+3
infix:<operand><operators><operands>, ((4*2)+3)
prefix:<operators><operands><operands>, +*4 2 3
postfix:<operands><operands><operators>, 4 2* 3+'''
def prefixevaluation(s):
    stack=[]
    for c in s[::-1]:
        if c.isdigit():
            stack.append(int(c))
        else:
            o1=stack.pop()
            o2=stack.pop()
            if c=='+':
                stack.append(o1+o2)
            if c=='-':
                stack.append(o1-o2)
            if c=='*':
                stack.append(o1*o2)
            if c=='/':
                stack.append(o1//o2)
    return stack.pop()
#print(prefixevaluation('+*423'))
'''class evaluate_postfix:
    def __init__(self):
        self.items=[]
        self.size=-1
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
        self.size+=1
    def pop(self):
        if self.isEmpty():
            return 0
        else:
            self.size-=1
            return self.items.pop()
    def seek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[self.size]
    def evalute(self,expr):
        for i in expr:
            if i in '0123456789':
                self.push(i)
            else:
                op1=self.pop()
                op2=self.pop()
                result=self.cal(op2,op1,i)
                self.push(result)
        return self.pop()
    def cal(self,op2,op1,i):
        if i == '*':
            return int(op2)*int(op1)
        elif i == '/':
            return int(op2)/int(op1)
        elif i == '+':
            return int(op2)+int(op1)
        elif i == '-':
            return int(op2)-int(op1)
s=evaluate_postfix()
expr=input('enter the postfix expression')
value=s.evalute(expr)
print('the result of postfix expression',expr,'is',value)'''
class infix_to_postfix:
    precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}#as certain operation have more precendence than others
    def __init__(self):
        self.items=[]
        self.size=-1
    def push(self,value):
        self.items.append(value)
        self.size+=1
    def pop(self):
        if self.isempty():
            return 0
        else:
            self.size-=1
            return self.items.pop()
    def isempty(self):
        if(self.size==-1):
            return True
        else:
            return False
    def seek(self):
        if self.isempty():
            return False
        else:
            return self.items[self.size]
    def isOperand(self,i):
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz':
            return True
        else:
            return False
    def infixtopostfix (self,expr):
        postfix=""
        print('postfix expression after every iteration is:')
        for i in expr:
            if(len(expr)%2==0):
                print("Incorrect infix expr")
                return False
            elif(self.isOperand(i)):
                postfix +=i
            elif(i in '+-*/^'):
                while(len(self.items)and self.precedence[i]<=self.precedence[self.seek()]):
                    postfix+=self.pop()
                self.push(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                o=self.pop()
                while o!='(':
                    postfix +=o
                    o=self.pop()
            print(postfix)
        while len(self.items):
            if(self.seek()=='('):
                self.pop()
            else:
                postfix+=self.pop()
        return postfix
#s=infix_to_postfix()
#expr=input('enter the expression ')
#result=s.infixtopostfix(expr)
#if (result!=False):
    #print("the postfix expr of :",expr,"is",result)
    def reverse(self,expr):
        rev=""
        for i in expr:
            if i == '(':
                i=')'
            elif i == ')':
                i='('
            rev=i+rev
        return rev
    def infixtoprefix (self,expr):
        prefix=""
        print('prefix expression after every iteration is:')
        for i in expr:
            if(len(expr)%2==0):
                print("Incorrect infix expr")
                return False
            elif(self.isOperand(i)):
                prefix +=i
            elif(i in '+-*/^'):
                while(len(self.items)and self.precedence[i] < self.precedence[self.seek()]):
                    prefix+=self.pop()
                self.push(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                o=self.pop()
                while o!='(':
                    prefix +=o
                    o=self.pop()
            print(prefix)
                #end of for
        while len(self.items):
            if(self.seek()=='('):
                self.pop()
            else:
                prefix+=self.pop()
                print(prefix)
        return prefix
s=infix_to_postfix()
expr=input('enter the expression ')
rev=""
rev=s.reverse(expr)
result=s.infixtoprefix(rev)
if (result!=False):
    prefix=s.reverse(result)
    print("the prefix expr of :",expr,"is",prefix)
    