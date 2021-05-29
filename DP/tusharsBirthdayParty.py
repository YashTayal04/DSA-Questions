class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
	def solve(self, A, B, C):
        dp = [1000000000000 for j in range(max(A)+1)]
        dp[0]=0
        for i in range(1,len(B)+1):
            for j in range(1,max(A)+1):
                if B[i-1]<=j:
                    dp[j]=min(dp[j],dp[j-B[i-1]]+ C[i-1])
                # print(dp)
        # print(dp)
        ans=0
        for i in A:
            ans+=dp[i]
        return ans