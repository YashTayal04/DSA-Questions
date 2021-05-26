class Solution:
	# @param A : list of list of integers
	# @return an integer
	def minPathSum(self, A):
        dp=[[0 for i in range(len(A[0]))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                dp[i][j]+=A[i][j]
                if i>0 and j>0:
                    dp[i][j]+=min(dp[i-1][j],dp[i][j-1])
                elif i>0:
                    dp[i][j]+=dp[i-1][j]
                elif j>0:
                    dp[i][j]+=dp[i][j-1]
        return dp[-1][-1]