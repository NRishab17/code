'''eg:[1,3,5,4,6,13,10,9,8,15,17]   17
                                  /     \
                               15       13
                               / \     / \
                              9   6    5 10
                             / \  / \
                            4 8   3 1
we need to build a Max-Heap from the above-given array elements. It can be clearly seen that the above complete binary tree formed does not follow the Heap property. So, the idea is to heapify the complete binary tree formed from the array in reverse level order following a top-down approach
So the idea is to find the position of the last non-leaf node and perform the heapify operation of each non-leaf node in reverse level order.
Last non-leaf node = Node at index ((n-1) - 1)/2= (n/2) - 1
Total Nodes = 11.
Last Non-leaf node index = (11/2) - 1 = 4.
Therefore, last non-leaf node = 6.
To build the heap, heapify only the nodes:
[1, 3, 5, 4, 6] in reverse order. 
Heapify 6: Swap 6 and 17
Heapify 4: Swap 4 and 9
Heapify 5: Swap 13 and 5.
Heapify 3: First Swap 3 and 17, again swap 3 and 15.
Heapify 1: First Swap 1 and 17, again swap 1 and 15, 
           finally swap 1 and 6.
'''
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1 
    r = 2 * i + 2 
    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l
    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)
def buildHeap(arr, n):
    startIdx = n // 2 - 1
    # Perform reverse level order traversal# from last non-leaf node and heapify each node
    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)
def printHeap(arr, n):
    for i in range(n):
        print(arr[i], end = " ")
arr = [ 1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17 ]
buildHeap(arr, len(arr))
printHeap(arr, len(arr))
''' maxheap is binary tree where value of parent>=childvalues mapping elements of heap into arraay is trivial as node at k index has left child at index2k+1 and right child at index 2k+2
The root element will be at Arr[0]. Below table shows indexes of other nodes for the ith node, i.e., Arr[i]:
Arr[(i-1)/2] Returns the parent node.Arr[(2*i)+1] Returns the left child node.Arr[(2*i)+2] Returns the right childnode.
 '''
import sys
class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1
    # Function to return the position of  parent for the node currently at pos
    def parent(self, pos):
        return pos // 2
    # Function to return the position of# the left child for the node currently    # at pos
    def leftChild(self, pos):
        return 2 * pos
    # Function to return the position of # the right child for the node currently # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1
    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False
    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])
    def maxHeapify(self, pos):
        # If the node is a non-leaf node and smallerthan any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or self.Heap[pos] < self.Heap[self.rightChild(pos)]):
                # Swap with the left child and heapifythe left child
                if (self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                # Swap with the right child and heapifythe right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size
        while (self.Heap[current] > self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)
    def Printheap(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + 
                  " LEFT CHILD : " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))
    # Function to remove and return the maximum element from the heap
    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
        return popped  
maxHeap = MaxHeap(15)
maxHeap.insert(5)
maxHeap.insert(3)
maxHeap.insert(17)
maxHeap.insert(10)
maxHeap.insert(84)
maxHeap.insert(19)
maxHeap.insert(6)
maxHeap.insert(22)
maxHeap.insert(9)
maxHeap.Printheap()
'''eg: we add 1 and 2 so median of this object is 1.5 as even no. of term we take average of middle values
    we add 3 to object then median is 2 as 2 is middle term of object for odd terms we take middle element as median
we add number and find median for that flow of input

'''
import heapq
class Median_Finder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    def add_Number(self, num):
        if not self.max_heap and not self.min_heap:#for inserting 1st element in max_heap and min_heap as their null before adding these values
            heapq.heappush(self.min_heap, num)
            return 
        if not self.max_heap:#inserting into max_heap which isnt empty
            if num > self.min_heap[0]:#check if num>1st value of min value
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))#pop value at minheap and add it in maxheap
                heapq.heappush(self.min_heap, num)#add value to min heap
            else:
                heapq.heappush(self.max_heap, -num)
            return
        if len(self.max_heap) == len(self.min_heap):#minheap matches maxheap in length
            if num < -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        elif len(self.max_heap) > len(self.min_heap):
            if num < -self.max_heap[0]:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if num > self.min_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
    def find_Median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0] 
S = Median_Finder()
S.add_Number(1)
S.add_Number(2)
result = S.find_Median()
print(result)
S.add_Number(3)
result = S.find_Median()
print(result)
S.add_Number(4)
S.add_Number(5)
result = S.find_Median()
print(result)
li = [5, 7, 9, 1, 3]
heapq.heapify(li)
print (list(li))
# using heappush() to push elements into heap pushes 4
heapq.heappush(li,4)
print (list(li))
print (heapq.heappop(li))# using heappop() to pop smallest element
li1 = [5, 7, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]
heapq.heapify(li1)
heapq.heapify(li2)
# using heappushpop() to push and pop items simultaneouslypops 2
print ("The popped item using heappushpop() is : ",end="")
print (heapq.heappushpop(li1, 2))
print(li1)  
# using heapreplace() to push and pop items simultaneouslypops 3
print(li2)
print ("The popped item using heapreplace() is : ",end="")
print (heapq.heapreplace(li2, 1))
print(li2)
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(li1)
# using nlargest to print 3 largest numbersprints 10, 9 and 8
print("The 3 largest numbers in list are : ",heapq.nlargest(3, li1),end="")
# using nsmallest to print 3 smallest numbers prints 1, 3 and 4
print("The 3 smallest numbers in list are : ",heapq.nsmallest(3, li1),end="")
'''heapq.heappush(heap,item) : Push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap) : Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
heapq.heappushpop(heap, item) : Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().
heapq.heapify(x) : Transform list x into a heap, in-place, in linear time.
heapq.merge(*iterables) : Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.'''
