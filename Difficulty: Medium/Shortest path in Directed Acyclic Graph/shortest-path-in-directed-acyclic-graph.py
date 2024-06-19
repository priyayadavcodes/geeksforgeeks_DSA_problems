from typing import List
from queue import LifoQueue

class Solution:
    def dfs(self, start_node, vis, adj, stack):
        vis[start_node] = 1
        for neighbor in adj[start_node]:
            if vis[neighbor] == 0:
                self.dfs(neighbor, vis, adj, stack)
        stack.put(start_node)
        
    def topoSort(self, V, adj):
        vis = [0 for i in range(V)]
        stack = LifoQueue(maxsize=V)
        for node in range(V):
            if vis[node] == 0:
                self.dfs(node, vis, adj, stack)
        ls = []
        while not stack.empty():
            ls.append(stack.get())
            
        return ls
    
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        for edge in edges:
            node_a = edge[0]
            node_b = edge[1]
            adj[node_a].append(node_b)
        
        topo = self.topoSort(n, adj)
        
        adj_with_weights = [[] for i in range(n)]
        for edge in edges:
            node_a = edge[0]
            node_b = edge[1]
            weight = edge[2]
            adj_with_weights[node_a].append([node_b, weight])
        
        dist = [float("inf") for i in range(n)]
  
        
        dist[0] = 0
        for node in topo:
            for neighbor, weight in adj_with_weights[node]:
                dist[neighbor] = min(dist[neighbor] ,dist[node] + weight)
        for i in range(len(dist)):
            if dist[i] == float("inf"):
                dist[i] = -1
        return dist
      
        
     


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends