#User function Template for python3
import math
class Solution:
    def switchCase(self, choice, arr):
        # Code here
        match choice:
            case 1:
                R=arr[0]
                return math.pi*R*R
            case 2:
                L,B=arr
                return L*B
            case _:
                return "invalid choice"
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        choice = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        if choice == 1:
            res = ob.switchCase(choice, arr)
            print("%.2f"%round(res,2))
        else:
            res = ob.switchCase(choice, arr)
            print(int(res))

# } Driver Code Ends