#Sort the array using insertion sort

class Solution:
    def insert(self, arr, index, n):

        for j in range(index,0,-1): # j must be greater than 0
            if arr[j-1]>arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
        
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, arr, n):
        for i in range(0,n):
            self.insert(arr,i,n)
        return arr
        
#{ 
 # Driver Code Starts

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends