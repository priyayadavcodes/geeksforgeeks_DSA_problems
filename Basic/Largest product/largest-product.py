# You are required to complete this fucntion
# Function should return the an integer
def findMaxProduct(arr, n, m):
    i,j = 0,0
    max_prod = float("-inf")
    prod = 1
    
    while j < n:
        prod = prod*arr[j]
        
        if j-i+1 < m:
            j = j+1
        else:
            max_prod = max(prod,max_prod)
            prod = prod//arr[i]
            i = i+1
            j = j+1
    return max_prod
    


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = map(int, input().strip().split(' '))
        arr = list(map(int, input().strip().split()))
        print (findMaxProduct(arr, n, m))
# } Driver Code Ends