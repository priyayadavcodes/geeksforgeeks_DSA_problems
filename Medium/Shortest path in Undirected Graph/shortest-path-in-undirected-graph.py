#User function Template for python3
from queue import Queue
class Solution:
    def adj_list(self,edges,n):
        ls = [[] for i in range(n)]
        for edge in edges:
            node_a = edge[0]
            node_b = edge[1]
            ls[node_a].append(node_b)
            ls[node_b].append(node_a)
        return ls
                

    
    def shortestPath(self, edges, n, m, src):
        dist = [-1 for i in range(n)]
        vis = [0 for i in range(n)]
        q = Queue(maxsize = n)
        q.put(src)
        vis[src] = 1
        dist[src] = 0
        
        adj = self.adj_list(edges,n)
        
        
        while q.empty() == 0:
            u = q.get()
            vis[u] = 1
          
            for node in adj[u]:
                if vis[node] ==0:
                    vis[node] = 1
                    dist[node] = dist[u]+1
                    q.put(node)
        return dist
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends