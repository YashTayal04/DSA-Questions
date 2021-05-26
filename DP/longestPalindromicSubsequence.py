class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        dp=[[0 for i in range(len(A))]for j in range(len(A))]
        for i in range(1,len(A)+1):
            for j in range(len(A)-i+1):
                if i==1:
                    dp[j][j]=1
                else:
                    if A[j]==A[j+i-1]:
                        dp[j][j+i-1]=2+dp[j+1][j+i-2]
                    dp[j][j+i-1]=max(dp[j][j+i-1],dp[j][j+i-2],dp[j+1][j+i-1])
        # print(dp)
        return dp[0][-1]