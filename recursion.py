#print n to 1
def backprint(n):
    if n==0:
        return
    print(n)
    backprint(n-1)
#backprint(5)
#sum of n natural numbers
def naturalsum(n,s=0):
    if n==0:
        print(s)
        return
    s+=n
    naturalsum(n-1,s)
#naturalsum(2,0)
def factorial(n,fact=1):
    if n==0:
        print(fact)
        return
    fact*=n
    factorial(n-1,fact)
#factorial(2,1)
def fibannoci(a,b,n):
    if n==0:
        return
    print(a)
    fibannoci(b,a+b, n-1)
#fibannoci(0, 1, 5)
#print x^n using x^n=x*(x^n-1) stack height=n
def power(x,n):
    if x==0:
        return 0
    if n==0:
        return 1
    a=power(x, n-1)
    b=x*a
    return b
#print(power(2,5))
'''2^5=2*2^4=2*2*2^3=2*2*2*2^2=2*2*2*2*2^1=2*2*2*2*2*2^0=32'''
#print x*n using x^n=x^(n/2)*x^(n/2) stack height=logn
def powerbylog(x,n):
    if x==0:
        return 0
    if n==0:
        return 1
    if n%2==0:
        return powerbylog(x, n//2)*powerbylog(x, n//2)
    else:
        return powerbylog(x, n//2)*powerbylog(x, n//2)*x
#print(powerbylog(2,2))
'''2^5=2^2*2^2*2=4*4*2=32 as 5//2=2 and x=2
   2^4=2^2*2^2=4*4=16  as 4//2=2 and x=2'''
def towerofhanoi(n,source,destination,auxiliary):
    if n==1:
        print('move disk 1 from source',source,'to destination',destination)
        return
    towerofhanoi(n-1,source,auxiliary,destination)
    print('move disk',n,'from source',source,'to destination',destination)
    towerofhanoi(n-1,auxiliary,destination,source)
#towerofhanoi(4, 'a','b','c')
        
        
def revstring(string,index):
    if index==0:
        print(string[index] ,end='')
        return
    print(string[index],end='')
    revstring(string,index-1)
#revstring('abcd',3)
first=-1
last=-1
def getindexes(string,element,index):
    if index==len(string):
        return
    if string[index]==element:
        global first
        global last
        if first==-1:
            first=index
        else:
            last=index
    getindexes(string, element, index+1)
'''getindexes('aabbccd','a',0)
print(first)
print(last)
first returns 1st occurrence and last returns last occurrance'''
def arrayincreasing(arr,index):
    if index==len(arr)-1:
        return True
    if not arrayincreasing(arr, index+1):
        return False
    return arr[index]<arr[index+1]
'''print(arrayincreasing([1,2,3,4],0))
[1,2,3,4] is strictly increasing
[1,2,2,3] is not strictly increasing but sorted
[3,2,1] is not increasing'''
def addxatlast(count):
    newstr=''
    for i in range(count):
        newstr+='x'
    return newstr
def movextolast(string,index,count):
    if index==len(string):
        return addxatlast(count)
    if string[index]=='x':
        return movextolast(string, index+1, count+1)
    else:
         newstr=movextolast(string, index+1, count)
         return string[index]+newstr 
#print(movextolast('abcd',0,0))
'''we find all x and increase count and using 
addxatlast function add x to last of string
if no x in string then return string with that 
last index element+newstr(which has previous elements of string)'''
def subsequences(string,index,result):
    if index==len(string):
        print(result)
        return
    #if element at that index joins
    subsequences(string, index+1, result+string[index])
    #if element at that index doesnt join
    subsequences(string, index+1, result)
#subsequences('abc',0,'')
'refer to subsequences notes'
s=[]
def removeduplicates(string,index):
    if index==len(string):
        return ''.join(s)
    if string[index] in s:
        removeduplicates(string, index+1)
    else:
        s.append(string[index])
        removeduplicates(string, index+1)
    return ''.join(s)
#print(removeduplicates('aabb',0))
'''we create s list which stores unique values of string in list
as we append those elements not in list and increase index or
increase index if already present in list'''
def findcombinations(keypad,keys,combinations,index,result):
    if index==-1:
        combinations.add(result)
        return
    digit=keys[index]
    length=len(keypad[digit])
    for i in range(length):
        findcombinations(keypad, keys, combinations, index-1,keypad[digit][i]+ result)
def findallcombinations(keypad,keys):
    if not keypad or not keys:
        return set()
    combinations=set()
    findcombinations(keypad, keys, combinations,len(keys)-1,'')
    return combinations
keypad={
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z']
                                }
keys=[2,3]
#print(findallcombinations(keypad, keys))

sn=[]
global m
m=0
def uniquesubsequences(string,list1,index1,index2):
    if index1==m:
        list1[index2]=None
        temp=''.join([i for i in list1 if i])
        sn.append(temp)
        return  ' '.join(set(sn))
    else:
        list1[index2]=string[index1]
        uniquesubsequences(string, list1, index1+1, index2+1)
        uniquesubsequences(string, list1, index1+1, index2)
        return ' '.join(set(sn)) 
string='ggg'
m=len(string)
n=int((2**m)+1)  
list1=[None for i in range(n)]
#print(uniquesubsequences(string, list1,0,0))  
    
        
        
    
    
    
        
        
        
    
    
    
    