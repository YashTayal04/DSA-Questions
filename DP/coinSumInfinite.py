class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B):
        dp=[0 for i in range(B+1)]
        for i in A:
            for j in range(B+1):
                if j==i:
                    dp[j]+=1
                elif j>i:
                    dp[j]+=dp[j-i]
                dp[j]%=1000007
        return dp[B]