class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):
        dp=[1,2]
        for i in range(3,A+1):
            dp.append(dp[-1]+dp[-2])
        return dp[A]