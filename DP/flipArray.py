class Solution:
	# @param A : tuple of integers
	# @return an integer
	def solve(self, A):
	    x=sum(A)//2
        dp=[len(A)+1 for i in range(x+1)]
        dp[0]=0
        for i in range(1, len(A)+1):
            for j in range(x,0,-1):
                if A[i-1]<=j:
                    dp[j]=min(dp[j],dp[j-A[i-1]]+1)
        for i in range(x,-1,-1):
            if dp[i]<=len(A):
                return dp[i]