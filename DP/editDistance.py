class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def minDistance(self, A, B):
        dp=[[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        for i in range(len(A)+1):
            for j in range(len(B)+1):
                if i==0 or j==0:
                    dp[i][j]=i+j 
                elif A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
        return dp[-1][-1]