class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def solve(self, A, B):
        dp=[0 for i in range(B+1)]
        for i in range(min(10,B+1)):
            dp[i]=1
        for i in range(2,A+1):
            temp=list(dp)
            for j in range(1,B+1):
                x=0
                for k in range(10):
                    if j-k>0:
                        x+=dp[j-k]
                        x%=1000000007
                temp[j]=x
            dp=temp
            # print(dp)
        return dp[B]