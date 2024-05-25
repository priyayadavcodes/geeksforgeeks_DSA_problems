class Solution:
    def select(self, arr, i):
        mini = i
        n = len(arr)
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        return mini

    def selectionSort(self, arr, n):
        for i in range(n):
            mini = self.select(arr, i)
            
            temp = arr[mini]
            arr[mini] = arr[i]
            arr[i] = temp
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends