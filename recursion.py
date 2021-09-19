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
def permutationsofstring(string,per):
    if len(string)==0:
        print(per)
        return
    for i in range(len(string)):
        curr=string[i]
        #from abc curr stores element at i index and adds it to newchar
        newstr=string[0:i]+string[i+1:]
        permutationsofstring(newstr,per+curr)
#permutationsofstring('abc','')
''' in abc possible combinations are abc,acb,bac,bca,cab,cba
3 string character so possible combinations=3!=6
time complexity is O(n!)'''
def paths(i,j,n,m):
    if i==n-1 and j==m-1:
        return 1
    if i==n or j==m:
        return 0
    #moving down
    downpaths=paths(i+1, j, n, m)
    #move right
    rightpaths=paths(i,j+1,n,m)
    return downpaths+rightpaths
#print(paths(0,0,3,3))
''' in a maze move from (0,0) to (n,m) where  we can move 
right or downward only
in our case we take n,m=3,3 total paths by logic is 6
every cell has 2 choices move right or down
but corner cell have only one choice
let our cell be at(i,j) sowe can move (i+1,j) or (i,j+1)
but at corner cell we have one option as 
i becomes n-1 then move only down or j becomes m-1move only right
we recursively find paths from certain cell to get to destination 
every times and find total by adding all paths'''        
def placetiles(n,m):
    if n==m:
        return 2
    if n<m:
        return 1
    verticalplacements=placetiles(n-m, m)
    horizontalplacements=placetiles(n-1, m)
    return verticalplacements+horizontalplacements
#print(placetiles(4, 2))
''' place tiles of 1*m in floor in size of n*m in our case n=4,m=2
place n tiles if vertically arranged then place n-m tiles
if horizontally then place n-1
base case is when n=m then ways=2 horizontally and vertically eg:n=2,m=2
n<m then ways=1 because only horizontal eg:n=2,m=4'''     
def callguests(n):
    if n<=1:
        return 1
    single=callguests(n-1)
    pairs=(n-1)*callguests(n-2)
    return single+pairs
#print(callguests(4))
'''finding no of ways in which invite n people to party in single or in pairs
eg: n=4 we have 10 ways and n=3 we have 4 ways
calling a guest single then call n-1 guests and if we pair n-1 choices then call
n-2 guests'''
def subsets(n,lists):
    if n==0:
        print(lists)
        return
    #add hoga
    lists.append(n)
    subsets(n-1,lists)
    #add nahi hoga
    lists.pop()
    subsets(n-1,lists)
#subsets(3,[])
'''print all subsets of n natural numbers eg:n=3
subset=(1,2,3),(1,2),(1,3),(2,3),(1),(2),(3),() O(2^n)'''

    
        
        
        
    
    
    
    