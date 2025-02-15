#User function Template for python3

class Solution:
    def toLower (self , s : str)-> str :
        # code here 
        s1=""
        for i in s:
            s1+=i.lower()
        return s1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s = input()
        
        ob = Solution()
        print(ob.toLower(s))
        print("~")
# } Driver Code Ends