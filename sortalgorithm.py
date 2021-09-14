def bubblesort(lists):
    size=len(lists)
    for i in range(size-1):
        swap=False
        for j in range(size-i-1):
            if lists[j]>lists[j+1]:
                lists[j],lists[j+1]=lists[j+1],lists[j]
                swap=True
        if not swap:
            break
'''def bubblesortfunction(lists,key):
    size=len(lists)
    if key=='name':
        for i in range(size-1):
            swap=False
            for j in range(size-i-1):
                if lists[j]['name']>lists[j+1]['name']:
                    lists[j]['name'],lists[j+1]['name']=lists[j+1]['name'],lists[j]['name']
                    swap=True
            if not swap:
                break
    elif key=='amount':
        for i in range(size-1):
            swap=False
            for j in range(size-i-1):
                if lists[j]['amount']>lists[j+1]['amount']:
                    lists[j]['amount'],lists[j+1]['amount']=lists[j+1]['amount'],lists[j]['amount']
                    swap=True
            if not swap:
                break
    elif key=='device':
        for i in range(size-1):
            swap=False
            for j in range(size-i-1):
                if lists[j]['device']>lists[j+1]['device']:
                    lists[j]['device'],lists[j+1]['device']=lists[j+1]['device'],lists[j]['device']
                    swap=True
            if not swap:
                break
a=[{'name':'mona','amount':1000,'device':'iphone'},
   {'name':'dhaval','amount':400,'device':'vivo'},
   {'name':'kathy','amount':200,'device':'oppe'},
   {'name':'amir','amount':800,'device':'iphone'}]
bubblesortfunction(a,'name')
print(a)'''
def insertionsort(lists):
    for i in range(1,len(lists)):
        key=lists[i]
        j=i-1
        while j>=0 and key<lists[j]:
            lists[j+1]=lists[j]
            j=j-1
        lists[j+1]=key
def selectionsort(lists):
    size=len(lists)
    for i in range(size-1):
        minindex=i
        for j in range(minindex+1,size):
            if lists[j]<lists[minindex]:
                minindex=j
        if i!=minindex:
            lists[i],lists[minindex]=lists[minindex],lists[i]
def swap(a,b,lists):
    if a!=b:
        lists[a],lists[b]=lists[b],lists[a]
def partition(lists,start,end):
    piv=start
    pivot=lists[piv]
    while start<end:
        while start<len(lists) and lists[start]<=pivot:
            start+=1
        while lists[end]>pivot:
            end-=1
        if start<end:
            swap(start,end,lists)
    swap(piv,end,lists)
    return end
def quicksort(lists,start,end):
    if start<end:
        pi=partition(lists,start,end)
        quicksort(lists,start,pi-1)
        quicksort(lists, pi+1, end)
def merge2list(list1,list2,list3):
    i=j=k=0
    while i<len(list1) and j<len(list2):
        if list1[i]<=list2[j]:
            list3[k]=list1[i]
            i+=1
        else:
            list3[k]=list2[j]
            j+=1
        k+=1
    while i<len(list1):
        list3[k]=list1[i]
        i+=1
        k+=1
    while j<len(list2):
        list3[k]=list2[j]
        j+=1
        k+=1
def merge1list(lists):
    if len(lists)<=1:
        return lists
    mid=len(lists)//2
    left=lists[:mid]
    right=lists[mid:]
    merge1list(left)
    merge1list(right)
    merge2list(left,right,lists)
'''a=[17,8,25,34,21]
merge1list(a)
print(a)'''
def shellsort(lists):
    size=len(lists)
    gap=size//2
    while gap>0:
        for i in range(gap,size):
            anchor=lists[i]
            j=i
            while j>=gap and lists[j-gap]>anchor:
                lists[j]=lists[j-gap]
                j-=gap
                lists[j]=anchor
        gap=gap//2
def countsort(lists):
    size=len(lists)
    output=[0]*size
    count=[0]*10
    for i in range(0,size):
        count[lists[i]]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i=size-1
    while i>=0:
        output[count[lists[i]]-1]=lists[i]
        count[lists[i]]-=1
        i-=1
    for i in range(0,size):
        lists[i]=output[i]
def heapify(lists,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and lists[i]<lists[l]:
        largest=l
    if r<n and lists[largest]<lists[r]:
        largest=r
    if largest!=i:
        lists[i],lists[largest]=lists[largest],lists[i]
        heapify(lists,n,largest)
def heapsort(lists):
    n=len(lists)
    for i in  range(n//2,-1,-1):
        heapify(lists,n,i)
    for i in range(n-1,0,-1):
        lists[i],lists[0]=lists[0],lists[i]
        heapify(lists,i,0)

        
            