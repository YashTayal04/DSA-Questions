def bs(A,x,r):
    l=0
    while l<=r:
        m=(l+r)//2
        if A[m]==x:
            return m
        elif A[m]>x:
            r=m-1
        else:
            l=m+1
    return -1

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A)<=2:
            return 0
        dp=[[2 for i in range(len(A))]for j in range(len(A))]
        ans=2
        for i in range(2,len(A)):
            for j in range(i):
                x=bs(A,A[i]-A[j],j-1)
                if x!=-1:
                    dp[j][i]=dp[x][j]+1
                    ans=max(ans,dp[j][i])
        if ans==2:
            return 0
        else:
            return ans
        