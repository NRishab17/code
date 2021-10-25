def reverselist(arr):
    start=0
    end=len(arr)-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
#print(reverselist([1,2,3]))
'''we swap start index value and end value to reverse the list eg:[1,2,3] start=0,end=2 so exchange 1 and 3 values start=1 and end=1 so final reverse list is [3,2,1]'''
def getmaxmin(arr,low,high):
    arrmin=arrmax=arr[low]
    if low==high:#if there is only one element
        return arrmax,arrmin
    elif high==low+1:#if there is only 2 element
        if arr[low]>arr[high]:
            arrmax=arr[low]
            arrmin=arr[high]
        else:
            arrmax=arr[high]
            arrmin=arr[low]
        return arrmax,arrmin
    else:
        mid=(low+high)//2
        arrmax1,arrmin1=getmaxmin(arr, low, mid)
        arrmax2,arrmin2=getmaxmin(arr, mid+1, high)
        return (max(arrmax1,arrmax2),min(arrmin1,arrmin2))
#print(getmaxmin([1,2,3],0,2))
'''we initialize arrmax,arrmin with low index for more than 2 element take mid value then get 2arrmax with mid has highvalue and low value similarly with arrmin get minvalues '''
def kthsmallelement(arr,start,end,k):
    if k>0 and k<=end-start+1:
        pos=partition(arr,start,end)
        if pos-start==k-1:#position is same as k
            return arr[pos]
        if pos-start>k-1:#position greater than k recur through left subarrat
            return kthsmallelement(arr, start, pos-1, k)
        return kthsmallelement(arr,pos+1,end, k-pos+start-1)#else recur through right subarray
def partition(arr,start,end):
    a=arr[end]
    i=start
    for j in range(start,end):
        if arr[j]<=a:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[end]=arr[end],arr[i]
    return i
#print(kthsmallelement([1,2,3,4,5,6,7],0,6,3))
'''paritition works as partition of quick sort assuming last element as pivot and moves all smaller element to left of it and greater eleemnts to right and return the index i of pivot such that array is sorted'''
def sort012(a,n):
    low=mid=0
    high=n-1
    while mid<high:
        if a[mid]==0:
            a[low],a[mid]=a[mid],a[low]
            low+=1
            mid+=1
        elif a[mid]==1:
            mid+=1
        else:
            a[mid],a[high]=a[high],a[mid]
            high-=1
    return a
#print(sort012([0,1,0,2,1,1],6))
'''traverse the array from start to end such that mid<high if mid index value is 0 push it low index and take low index value in mid and low+=1 and mid+=1if mid index value=1 then update mid as we want 1 to be near mid of the table if mid index value=2 then swap it with high index value so to keep 2 at rear end of list high-=1
0's are near low index value 1's are near the mid of array and 2's in high index/rear end of array'''
def rearrangearray(arr,n):
    j=0
    for i in range(0,n):
        if arr[i]<0:#if value is negative
            arr[i],arr[j]=arr[j],arr[i]#exchange the values to starting with i and j th index are exchanged
            j+=1
    return arr
#print(rearrangearray([1,2,3,-4,5],5))we move negative values to start of array
def printunion(arr1,arr2):
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            print(arr1[i])#ith value is low so printed first
            i+=1
        elif arr2[j]<arr1[i]:
            print(arr2[j])#jth value is low so printed
            j+=1
        else:
            print(arr2[j])#print remaining values of j
            i+=1
            j+=1
    while i<len(arr1):#printing remaining elementd of larger array
        print(arr1[i])
        i+=1
    while j<len(arr2):
        print(arr2[j])
        j+=1
#printunion([1,2,4,5,6],[2,3,5,7])
def  rotate(arr,n):
    x=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=x
    return arr
#print(rotate([1,2,3],3))
'store last element in x then push all elements by one positition ahead and replace first eleemnt with x'
def largestsumarray(arr,n):
    maxsofar=-10000000000#take large value so 1st value is replaced easly
    maxend=0
    for i in range(0,n):
        maxend=maxend+arr[i]
        if maxsofar<maxend:
            maxsofar=maxend
        if maxend<0:#for negative value reset maxend value
            maxend=0
    return maxsofar
#print(largestsumarray([1,2,3,-6],4))
'''look for positive numbers and keep track of maximum sum contigous segment among all positive segments each time we get positive sum compare it with maxsofar and add it to maxsofar if its>maxsofar'''
def getmindiff(arr,n,k):
    if n==1:
        return 0
    arr.sort()
    ans=arr[n-1]-arr[0]
    small=arr[0]+k
    big=arr[n-1]-k
    if small>big:
        small,big=big,small
    for i in range(1,n-1):
        subtract=arr[i]-k
        add=arr[i]+k
        if subtract>=small or add<=big:
            continue
        if big-subtract<=add-small:
            small=subtract
        else:
            big=add
    return min(ans,big-small)
#print(getmindiff([4,6], 2, 10))
'''modify array by subtracting/adding k to every element such that differenece between maximum and minimum is minimized 
we initilaize result by subtract last-first element handle corner elements as small and big by addin 1st element iwth k and last element - k
if small>big then exchange values traverse middle values if both subtraction and addition dont change the differeence 
either subtraction causes smaller number or addititon causes greater number update small/big using this if big-subtract causes smaller diff update small else update big'''
def duplicates(arr,size):
    for i in range(0,size):
        if arr[abs(arr[i])]>=0:
            arr[abs(arr[i])]=-arr[abs(arr[i])]
        else:
            print(abs(arr[i]))
#duplicates([1,2,3,3,2,1],6)
'traverse the array for every element takes its absolute value if abs(arr[i]) is positive element hs been encountered before else if negative eleemnt has been encountered before print absolute value of current element'
def merge(a,b):
    for i in range(len(a)):#traverse e1st array and check for each element
        if a[i]>b[0]:
            a[i],b[0]=b[0],a[i]#shift b[0] to its correct position in second array
            j=0
            while j+1<len(b) and b[j]>b[j+1]:#shift elements with b also correctly
                b[j],b[j+1]=b[j+1],b[j]
                j+=1
    print(a)
    print(b)
#merge([1,2,4],[3,5,6])
def mergeintervals(arr):
    arr.sort()
    ans=[]
    for s,e in arr:
        if ans and s<=ans[-1][1]:
            ans[-1][1]=max(ans[-1][1],e)
        else:
            ans.append([s,e])
    print(ans)
#mergeintervals([[1,4],[2,6]])
'''sort the list and create new list ans for each start and end in arr if s<ans last elements 1st element then bigger interval with ans[1][1],e is created'''
def nextpermutate(arr):
    a=list(arr)
    for i in range(-1,-len(arr)+1,-1):
        if arr[i]>arr[i-1]:
            arr[i],arr[i-1]=arr[i-1],arr[i]
            break
    if arr!=a:    
        return arr
    else:
        a.sort()
        return a
#print(nextpermutate([3,2,1]))
'''we take a=list(arr) we iterate in reverese order if last element>2nd last element then exchange value so we get next permutate of list values'''
def countinversion(arr):
    count=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]>arr[j] and i<j:
                count+=1
    return count
#print(countinversion([3,2,1]))
'''count iversion is no of steps needed to sort the list'''
def maxprofit(arr):
    ans=0
    for i in range(1,len(arr)):
        if arr[i]-arr[i-1]>0:
            ans+=(arr[i]-arr[i-1])
    return ans
#print(maxprofit([7,1,6,5,4]))
'''we have array of stock prices we need to find when to buy and sell stock so maximum profit is possible constrait: we cant sell stock before buying it eg:[7,1,6]  actually maximum profit is obtained when we buy at 1 and sell at 7 but 7 price was available a day before so we cant sell before buying it that why maximum  profit is 5 as we can buy for 1 and sell it for 7'''
def sumarray(arr,k):
    d={}
    for i,e in enumerate(arr):
        if k-e in d:
            print(arr[d.get(k-e)],arr[i])
        d[e]=i
    return
#sumarray([1,5,7,-1],6)
'''we make d dictionary with e as keys and i as values then traverse such that i stores index value of array and e stores actucal value of element in arrayif k(target)-e is presnt in d then print arr([k-e]th index(key)i) with arr[i] and store e as key and i as value in dictionary so repetattion can be avoided'''
def commomeleemnts(arr1,arr2,arr3):
    arr1=set(arr1)
    arr2=set(arr2)
    arr3=set(arr3)
    arr1=arr1.intersection(arr2)
    arr1=arr1.intersection((arr3))
    return list(arr1)
#print(commomeleemnts([10,101,20],[10,101,20,2,34],[20,10]))
def rearrange(arr):
    arr.sort()
    i=j=1
    while j<len(arr):
        if arr[j]>0:
            break           
        j+=1
    while (arr[i]<0) and (j<len(arr)):
        arr[i],arr[j]=arr[j],arr[i]
        i+=2
        j+=1
    return arr 
#print(rearrange([5,-2,-3,4,5]))
'''we need to keep negative numbers at even index of list and positive numebrs at odd indexes of list so sort the list first  j pointer points positive value and i points negative value becuase we break loops as soon as arr[j]>0 then swaps its value iwth negative value available in the list making them be in even indexes and  increase i by 2 as i is negative index pointer'''
def sumis0(arr):#it is same as sumarray of k=0
    d={}
    for i,e in enumerate(arr):
        if 0-e in d:
            print('yes')
        d[e]=i
    return
#sumis0([1,-1,5,3])
def factorial(n):
    if n<=1:#base case
        return n
    else:
       return  n*factorial(n-1)
#print(factorial(5))
def maxproduct(arr,n):
    maxendhere=minendhere=1#max positive product ending at cuurent position and min positive product ending at cuurent position 
    maxsofar=flag=0
    for i in range(n):#traverse through array  check maxendhere is alaway maxproduct ending with arr[i] or 1 minendhere is always negative product with arr[i] or 1
        if arr[i]>0:#if element is positive update max end here and minendhere
            maxendhere=maxendhere*arr[i]
            minendhere=min(minendhere*arr[i],1)
            flag=1
        elif arr[i]==0:#if eleemnt is zero maxendhere and minendhere cant here as value is greater than or equal to 1
             maxendhere=minendhere=1
        else:#if eleemnt is negative max end can be either be 1 or positive  min end can either be negative or 1 next min end can here will always be prev maxendhere*arr[i] next max  end here will be 1 if prev   minendhere is 1 otherwise next maxend here will be  p minendhere*arr[irev
             temp= maxendhere
             maxendhere=max(minendhere*arr[i],1)
             minendhere=temp*arr[i]
        if maxsofar<maxendhere:
            maxsofar=maxendhere
    if flag==0 and maxsofar==0:
        return 0
    return maxsofar
#print(maxproduct([0,10,6,-2,0],5))'''eg:[1,2,0,-3,-10] in this -3,-10 can give max product as contigious subarray '''
def longestconseqsubseq(a):
    a=set(a)
    maxlength=0
    for i in a:
        if i-1 not in a:
            length=1
            while i+length in a:
                length+=1
            maxlength=max(maxlength,length)
    return maxlength
#print(longestconseqsubseq([1,0,2,4,3]))    
''' we nedd to find logest subsequence that are consecutive in given array eg:[1,7,8,55,2,3] has 3 with [1,2,3] as largest subsequence
make set out of array now iterate through every element in a if i is candidate for starting sequence as i-1 doesnt exist in the set then length of subsequence get value 1 (as i is starting value) then check for i+1,i+2...i+length available in set or not  then return maxlength as maximum value of maxlength and length'''
def morethannbyk(arr,n,k):
    x=n//k
    freq={}
    for i in range(n):
        if arr[i] in freq:
               freq[arr[i]]+=1
        else:
            freq[arr[i]]=1
    for i in freq:
        if freq[i]>x:
            print(i)
#morethannbyk([1,1,1],3, 2)
'''we have to show values whose frequency is more than n/k so x=n//k and freq dictinary created iterate over it  if arr[i] already exist increase its frequency or add it to freq{} then print all values in freq{} greater than x'''
def maxwater(arr):
    n=len(arr)
    left=result=lmax=rmax=0
    right=n-1
    while left<=right:#we need to check for mininmum of left and right max for every element 
        if rmax<=lmax:#add difference between current element and right value 
            result+=max(0,rmax-arr[right])
            rmax=max(rmax,arr[right])#update rightmax
            right-=1#update right pointer
        else:
            result+=max(0,lmax-arr[left])#similar to right we do for left
            lmax=max(lmax,arr[left])
            left+=1
    return result
#print(maxwater([0,1,0,2,1,0,1,3,2,1,2,1]))
'''at every index amount of rainwatre stored is difference between current index height and minimum of leftmaxheight and rightmaxheight
 given n non negative integers representing elevation map whree the width of bar is 1 comput how much watre can be stored between two bars 0 represnt the block is empty and 2 reperesent there is 2 block height bar
 eg:[2,0,2] we can trap 2 units of water as its suurounded by 2 units height block bars on left and right'''
def chocolatedis(arr,n,m):
    if m==0 or n==0:#if no of students or chocolates are 0
        return 0
    arr.sort()
    if n<m:# as students cant be more than number of packets
        return -1
    mindiff=arr[n-1]-arr[0]
    for i in range(len(arr)-m+1):
        mindiff=min(mindiff,arr[i+m-1]-arr[i])
    return mindiff
#print(chocolatedis([12,4,7,9,2,23,25,41,30,40,28,42,30,44,48,43,50],17, 7))   
'''array of n integers where each value represent chocolates in packet divided among m students such that eaxh gets one packet differeence between no of maximum chocollates and minimum chocolates given to students is minimum
find the subarray of size m such that difference between last(maximum) and first(minimum) elements of subarray is minimum'''
def partittion3way(arr,n,low,high):
    start=i=0
    end=n-1
    while i<=end:#traverse from left of array
        if arr[i]<=low:#lower than low are put at beginning of array
            temp=arr[i]
            arr[i]=arr[start]
            arr[start]=temp
            i+=1
            start+=1
        elif arr[i]>high:#greater than high are put at end of arrray
            temp=arr[i]
            arr[i]=arr[end]
            arr[end]=temp
            end-=1
        else:#all other reamain at same positition as before
            i+=1
a=[1,5,3,4,2]
partittion3way(a, 5, 3, 4)
#print(a)
'''given an array and range(low,high) partition around the range sucthat all elements lowr than low come first all element in range of low and high come next and all element greater than high appera in end '''
def palindrome(n):
    str1=str(n)
    len1=len(str1)
    for i in range(int(len1/2)):
        if str1[i]!=str1[len1-1-i]:#if 1st and last index character are not same then not a palindrome similarly for 2nd and 2nd last....
            return False
    return True
def palindromearray(arr,n):
    for i in range(n):
        ans=palindrome(arr[i])
        if ans==False:
            return False
    return True
#print(palindromearray([111,122], 2))
'''given an array which have numbers return 1 if all elements in array in palindrome eg:[111,222,323,414] return one as elements in array are palindrome [121,343,556] return0 as 3rd element is not palindrome'''
def medianof2array(arr1,arr2):
    arr=arr1+arr2
    arr.sort()
    mid=len(arr)//2
    if len(arr)%2!=0:
        result=arr[mid]
    else:
        result=(arr[mid]+arr[mid+1])/2
    return result
#print(medianof2array([1,3],[2]))

        
    