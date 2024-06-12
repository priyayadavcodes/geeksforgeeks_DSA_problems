#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        
        sortarr = arr.sort()
        ln = len(arr)
        num = arr[0]
        
        if arr[0] != 1:
            return 1
 
        for i in range(1,ln):
            if num+1 != arr[i]:
                return num+1
            else:
                num = arr[i]
        
        return n    
       
   
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends