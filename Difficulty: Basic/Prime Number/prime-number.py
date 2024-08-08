#User function Template for python3
import math
class Solution:
    def isPrime (self, N):
        # code here
        if N <=1:
            return 0
        if N<=3:
            return 1
        if N%2==0:
            return 0
            
        for i in range(3, int(math.sqrt(N)) + 1,2):
            if N%i==0:
                return 0
            
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends