class Solution:
	# @param A : integer
	# @return an integer
	def countMinSquares(self, A):
        dp=[0,1]
        for i in range(2,A+1):
            dp.append(i)
            j=1
            while i-j*j>=0:
                dp[i]=min(dp[i],dp[i-j*j]+1)
                j+=1
        return dp[A]