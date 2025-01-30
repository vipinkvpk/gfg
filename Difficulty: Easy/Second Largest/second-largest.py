#User function Template for python3

class Solution:
    def getSecondLargest(self, arr):
        if len(arr)<2:
            return "There are no enorgh array elements"
        # Code Here
        largest=second_largest=float('-inf')

        for i in arr:
            if i > largest:
                second_largest=largest
                largest=i
            elif i > second_largest and i != largest:
                second_largest=i
        return second_largest if second_largest != float('-inf') else -1

        # if second_largest!=float('-inf'):
        #     return second_largest
        # else:
        
        #     return "there is no second largest elemetn"


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends