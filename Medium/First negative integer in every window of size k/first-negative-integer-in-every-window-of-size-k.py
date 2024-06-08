#User function Template for python3

def printFirstNegativeInteger( A, N, K):

    i, j = 0, 0
    ls = []
    negatives = []

    while j < N:
        
        if A[j] < 0:
            negatives.append(A[j])
            
        if j - i + 1 < K:
            j = j+1
            
        else:
            if negatives:
                ls.append(negatives[0])
            else:
                ls.append(0)

            
            if A[i] < 0:
                negatives.pop(0)

            i += 1
            j += 1

    return ls

                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends