#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        maxele = float("-inf")
        maxls = []
      
        ls = []
        i ,j = 0,0
        
        while j < n:
            
            if arr[j] > maxele:
                maxele = arr[j]
                
                
            if j-i+1 < k:
                j +=1
            else:
                ls.append(maxele)

                if arr[i] == maxele:
                    maxele = float("-inf")
                    for x in range(i + 1, j + 1):
                        if arr[x] > maxele:
                            maxele = arr[x]
                i += 1 
                j += 1
        return ls
        
        
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends