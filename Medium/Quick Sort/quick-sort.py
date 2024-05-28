#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low < high:
            part_index= self.partition(arr,low,high)
            self.quickSort(arr,low,part_index-1)
            self.quickSort(arr,part_index+1,high)
        
    
    def partition(self,arr,low,high):
        pivot = arr[high]
        i = low
        j = high
        while(i<j):
            while arr[i] < pivot and i<=high-1:
                i = i+1
            while arr[j] >= pivot and j>=low+1:
                j = j-1
            if i < j:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                
        temp = arr[high]
        arr[high] = arr[i]
        arr[i] = temp
            
        return i
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends