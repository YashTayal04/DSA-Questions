class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        dp=[0,1,2]
        for i in range(3,A+1):
            dp.append((dp[-1]+(i-1)*dp[-2])%10003)
        return dp[A]