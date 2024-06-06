from typing import List
from collections import deque

class Solution:
    
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        # Initialize indegree array to store the number of incoming edges for each vertex
        indegree = [0] * V
        
        # Compute indegrees of all vertices
        for u in range(V):
            for node in adj[u]:
                indegree[node] += 1
        
        # Initialize a deque to store vertices with no incoming edges
        q = deque()
        
        # Enqueue all vertices with indegree 0
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        # Counter to keep track of the number of vertices processed
        cnt = 0
        
        # Process the queue
        while q:
            u = q.popleft()  # Dequeue a vertex with indegree 0
            cnt += 1  # Increment the count of processed vertices
            
            # Reduce the indegree of adjacent vertices
            for node in adj[u]:
                indegree[node] -= 1
                # If indegree becomes 0, add the vertex to the queue
                if indegree[node] == 0:
                    q.append(node)
        
        # If count of processed vertices is equal to the number of vertices, no cycle
        return cnt != V



            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

# } Driver Code Ends