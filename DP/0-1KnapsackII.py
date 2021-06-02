class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        dp=[1000000000 for i in range(sum(A)+1)]
        dp[0]=0
        for i in range(1,len(A)+1):
            for j in range(sum(A),0,-1):
                if A[i-1]<=j:
                    dp[j]=min(dp[j],dp[j-A[i-1]]+B[i-1])
        # print(dp)
        for i in range(sum(A),-1,-1):
            if dp[i]<=C:
                return i