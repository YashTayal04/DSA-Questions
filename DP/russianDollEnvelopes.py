class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        dp=[1 for i in range(len(A))]
        for i in range(1,len(A)):
            for j in range(i):
                if A[i][0]>A[j][0] and A[i][1]>A[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)