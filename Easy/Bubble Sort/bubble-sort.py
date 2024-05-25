#User function Template for python3

class Solution:
    def bubbleSort(self,arr, n):
        for i in range(n-1,0,-1):
            count = 0
            if count != 0:
                break
            else:
                for j in range(0,i):
                    if arr[j]>arr[j+1]:
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
                    else:
                        count = count+1
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends