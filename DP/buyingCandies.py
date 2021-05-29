class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        dp = [0 for i in range(D+1)]
        for i in range(1,D+1):
            for j in range(1,len(A)+1):
                if C[j-1]<=i:
                    dp[i]=max(dp[i],dp[i-C[j-1]]+B[j-1]*A[j-1])
        # print(dp)
        return dp[-1]