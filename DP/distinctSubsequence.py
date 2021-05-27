class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def numDistinct(self, A, B):
        dp=[[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        for i in range(len(A)+1):
            dp[i][0]=1
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    dp[i+1][j+1]+=dp[i][j]
                dp[i+1][j+1]+=dp[i][j+1]
        return dp[-1][-1]