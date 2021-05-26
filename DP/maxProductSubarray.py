class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProduct(self, A):
        dp=[(A[0],A[0])]
        for i in A[1:]:
            dp.append((min(i,i*dp[-1][0],i*dp[-1][1]),max(i,i*dp[-1][0],i*dp[-1][1])))
        ans=dp[0][1]
        for i in dp:
            ans=max(ans,i[1])
        return ans
                