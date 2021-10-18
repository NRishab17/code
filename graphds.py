class AdjNode:#adjacency list format
    def __init__(self, data):
        self.vertex = data
        self.next = None
# A class to represent a graph. A graph is the list of the adjacency lists. Size of the array will be the no. of the vertices "V"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        node = AdjNode(dest)# Adding the node to the source node
        node.next = self.graph[src]
        self.graph[src] = node
        node = AdjNode(src)# Adding the source node to the destination asit is the undirected graph
        node.next = self.graph[dest]
        self.graph[dest] = node
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
V = 5
graph = Graph(V)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.print_graph()
''' 1)Adjacency Matrix: Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph. Let the 2D array be adj[][], a slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j. Adjacency matrix for undirected graph is always symmetric. Adjacency Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w. 
Pros: Representation is easier to implement and follow. Removing an edge takes O(1) time. Queries like whether there is an edge from vertex ‘u’ to vertex ‘v’ are efficient and can be done O(1).
Cons: Consumes more space O(V^2). Even if the graph is sparse(contains less number of edges), it consumes the same space. Adding a vertex is O(V^2) time. 
Please see this for a sample Python implementation of adjacency matrix.
2)Adjacency List: An array of lists is used. The size of the array is equal to the number of vertices. Let the array be an array[]. An entry array[i] represents the list of vertices adjacent to the ith vertex. This representation can also be used to represent a weighted graph. The weights of edges can be represented as lists of pairs. Following is the adjacency list representation of the above graph.'''
from collections import defaultdict
class Graph:#This class represents a directed graph using adjacency list representation
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        queue = []
        # Mark the source node asvisited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue: # Dequeue a vertex fromqueue and print it
            s = queue.pop(0)
            print (s, end = " ")
            # Get all adjacent vertices of thedequeued vertex s. If a adjacenthas not been visited, then mark itvisited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print ("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2) 
'''Breadth first search is a graph traversal algorithm that starts traversing the graph from root node and explores all the neighbouring nodes. Then, it selects the nearest node and explore all the unexplored nodes. The algorithm follows the same process for each of the nearest node until it finds the goal.The algorithm of breadth first search is given below. The algorithm starts with examining the node A and all of its neighbours. In the next step, the neighbours of the nearest node of A are explored and process continues in the further steps. The algorithm explores all neighbours of all the nodes and ensures that each node is visited exactly once and no node is visited twice.
Breadth-First Search Algorithm or BFS is the most widely utilized method
BFS is a graph traversal approach in which you start at a source node and layer by layer through the graph, analyzing the nodes directly related to the source node. Then, in BFS traversal, you must move on to the next-level neighbor nodes.
According to the BFS, you must traverse the graph in a breadthwise direction:
To begin, move horizontally and visit all the current layer's nodes.Continue to the next layer.bredth-first-search-in-graph-data-structure
Breadth-First Search uses a queue data structure to store the node and mark it as "visited" until it marks all the neighboring vertices directly related to it. The queue operates on the First In First Out (FIFO) principle, so the node's neighbors will be viewed in the order in which it inserts them in the node, starting with the node that was inserted first.'''
'''Depth first search (DFS) algorithm starts with the initial node of the graph G, and then goes to deeper and deeper until we find the goal node or the node which has no children. The algorithm, then backtracks from the dead end towards the most recent node that is yet to be completely unexplored.
The data structure which is being used in DFS is stack. The process is similar to BFS algorithm. In DFS, the edges that leads to an unvisited node are called discovery edges while the edges that leads to an already visited node are called block edges.
Algorithm:
Step 1: SET STATUS = 1 (ready state) for each node in G
Step 2: Push the starting node A on the stack and set its STATUS = 2 (waiting state)
Step 3: Repeat Steps 4 and 5 until STACK is empty
Step 4: Pop the top node N. Process it and set its STATUS = 3 (processed state)
Step 5: Push on the stack all the neighbours of N that are in the ready state (whose STATUS = 1) and set their
STATUS = 2 (waiting state) and exit'''
import numpy as np
# DFS is called recusrively untill all nodes of given graph are traversed
def DFS(vertex) :
    if visited[vertex] == None :
        print(vertex)
        visited[vertex] = 1
        for x in range(vertices) :
            if visited[x] == None and adjacency_matrix[vertex][x] == 1 :
                DFS(x)
    else :
        return
vertices = int(input("enter number of vertices present in graph :- "))
visited = np.array([None]*vertices)
adjacency_matrix = [[0,1,1,1,0,0,0],
                    [1,0,1,0,0,0,0],
                    [1,1,0,1,1,0,0],
                    [1,0,1,0,1,0,0],
                    [0,0,1,1,0,1,1],
                    [0,0,0,0,1,0,0],
                    [0,0,0,0,1,0,0]]# This adjacency matrix represents the graph shown in example above
DFS(0)# You can choose any vertex of gievn graoh as the starting vertex