class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        dp=[[1000000000 for i in range(len(A))] for j in range(len(A))]
        for i in range(len(A)):
            dp[i][i]=0
        for i in range(len(A)-2):
            dp[i][i+1]=A[i]*A[i+1]*A[i+2]
        for i in range(3,len(A)):
            for j in range(len(A)-i):
                for k in range(j,j+i-1):
                    dp[j][j+i-1]=min(dp[j][j+i-1],dp[j][k]+dp[k+1][j+i-1]+ A[j]*A[k+1]*A[j+i])
        # print(dp)
        return dp[0][len(A)-2]
        