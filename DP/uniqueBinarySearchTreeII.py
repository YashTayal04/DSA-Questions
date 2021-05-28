class Solution:
	# @param A : integer
	# @return an integer
	def numTrees(self, A):
        dp=[1,1]
        for i in range(2,A+1):
            x=0
            for j in range(i):
                x+=dp[j]*dp[i-1-j]
            dp.append(x)
        return dp[A]