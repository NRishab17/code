#finding element in 2d array
n=int(input('no of rows'))
m=int(input('no of columns'))
target=int(input('element to find'))
lists=[[1,4,7,11],
       [2,5,8,12],
       [3,6,9,16],
       [10,13,14,17]]
found=False
r,c=0,n-1
while r<m and c>=0:
    if lists[r][c]==target:
        found=True
        break
    if lists[r][c]>target:
        c-=1
    else:
        r+=1
if found:
    print('found')
else:
    print('not found')
#matrix multiplication
'''given 2 array of n1*n2 and n2*n3 find new matrix of order n1*n3'''
list1=[[2,4,1,2],
       [8,4,3,6],
       [1,7,9,5]]
list2=[[1,2,3],
       [4,5,6],
       [7,8,9],
       [4,5,6]]
list3=[[0,0,0],
       [0,0,0],
       [0,0,0],]
n1,n2,n3=3,4,3
for i in range(n1):
    for j in range(n3):
        for k in range(n2):
            list3[i][j]+=list1[i][k]*list2[k][j]
for i in range(n1):
    for j in range(n3):
        print(list3[i][j],end=' ')
    print()
#largest word in a sentence
inp=list(input().split())
i=maxlength=0
while i<len(inp):
    word=inp[i]
    length=len(inp[i])
    if length>maxlength:
        maxlength=length
        string=inp[i]
    i+=1
print(maxlength)
print(string)
