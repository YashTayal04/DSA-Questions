class Solution:
	# @param A : integer
	# @return an integer
	def chordCnt(self, A):
        dp=[1,1]
        for i in range(2, A+1):
            x=0
            for j in range(i):
                x+=dp[j]*dp[i-1-j]
                x%=1000000007
            dp.append(x)
        return dp[-1]