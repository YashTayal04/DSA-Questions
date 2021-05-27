class Solution:
	# @param A : string
	# @return an integer
	def anytwo(self, A):
        dp=[[0 for i in range(len(A)+1)]for i in range(len(A)+1)]
        for i in range(1,len(A)+1):
            for j in range(1,len(A)+1):
                if A[i-1]==A[j-1] and i!=j:
                    dp[i][j]=1+dp[i-1][j-1]
                dp[i][j]=max(dp[i][j],dp[i-1][j],dp[i][j-1])
        if dp[len(A)][len(A)]>=2:
            return 1
        else:
            return 0