#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        maxsum = float("-inf")
        sum = 0
        i = 0
        j =0
        while j < N:
            sum = sum+Arr[j]
            if j-i+1 <K:
                j = j+1
            else:
                maxsum = max(sum,maxsum)
                sum = sum-Arr[i]
                i = i+1
                j = j+1
        return maxsum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends