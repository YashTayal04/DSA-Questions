class Solution:
	# @param A : list of list of integers
	# @return an integer
	def maximalRectangle(self, A):
        for i in range(len(A)):
            for j in range(1,len(A[0])):
                if A[i][j]==1:
                    A[i][j]+=A[i][j-1]
        dp=[[0 for i in range(len(A[0]))] for j in range(len(A))]
        for i in range(len(A[0])):
            dp[0][i]=A[0][i]
        for i in range(1,len(A)):
            for j in range(len(A[0])):
                mi=A[i][j]
                dp[i][j]=mi
                for k in range(i-1,-1,-1):
                    mi=min(mi,A[k][j])
                    dp[i][j]=max(dp[i][j],mi*(i-k+1))
        ans=0
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans=max(ans,dp[i][j])
        return ans