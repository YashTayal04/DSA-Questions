class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        dp=[[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        dp[0][0]=1 
        for i in range(1,len(B)+1):
            if B[i-1]=='*':
                dp[0][i]=1
            else:
                break
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1]==B[j-1] or B[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                elif B[j-1]=='*':
                    dp[i][j]=dp[i][j-1] | dp[i-1][j]
        # print(dp)
        return dp[-1][-1]