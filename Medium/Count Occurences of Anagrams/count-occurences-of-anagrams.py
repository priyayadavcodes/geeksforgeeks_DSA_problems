#User function Template for python3
class Solution:

	
	def search(self, pat, txt):
        lstext = list(txt)
        lspat = list(pat)
        N = len(lstext)
        k = len(lspat)
        i, j = 0, 0
        ans = 0
    
        unq_ele = set(pat)
        ele_cnts = {element: pat.count(element) for element in unq_ele}
        count = len(ele_cnts)
    
        while j < N:
            if lstext[j] in ele_cnts:
                ele_cnts[lstext[j]] -= 1
                if ele_cnts[lstext[j]] == 0:
                    count -= 1
    
            if j - i + 1 < k:
                j += 1
            else:
                if count == 0:
                    ans += 1
                if lstext[i] in ele_cnts:
                    if ele_cnts[lstext[i]] == 0:
                        count += 1
                    ele_cnts[lstext[i]] += 1
                i += 1
                j += 1
        return ans

                
                
                    
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends