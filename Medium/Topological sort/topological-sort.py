from queue import LifoQueue

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        vis = [0 for i in range(V)]
        stack = LifoQueue(maxsize=V)
        ls = []
        for node in range(V):
            if vis[node] == 0:
                self.dfs(node,vis,adj,stack)
                
        while stack.empty() == False:
            a = stack.get()
            ls.append(a)
            
            
        return ls
                
    def dfs(self,start_node,vis,adj,stack):
        vis[start_node] = 1
        
        for node in adj[start_node]:
            if vis[node] == 0:
                self.dfs(node,vis,adj,stack)
                
        stack.put(start_node)
        
        
        



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends