class Solution:
	# @param A : string
	# @param B : string
	# @param C : string
	# @return an integer
	def isInterleave(self, A, B, C):
        dp=[[ 0 for i in range(len(A)+1)] for i in range(len(B)+1)]
        if len(C)!=len(A)+len(B):
            return 0
        dp[0][0]=1
        for i in range(0,len(A)+1):
            for j in range(0,len(B)+1):
                    if i>0 and A[i-1]==C[i+j-1]:
                        dp[j][i]=dp[j][i-1]
                    if j>0 and B[j-1]==C[i+j-1]:
                        dp[j][i]=dp[j][i] | dp[j-1][i]
        # print(dp)
        return dp[-1][-1]