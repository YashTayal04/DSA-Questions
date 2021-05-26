def bs(a,i):
    l=0
    r=len(a)
    while l<r:
        m=(l+r)//2
        if a[m]==i:
            return m
        elif a[m]<i:
            l=m+1
        else:
            r=m
    return l

class Solution:
    # @param A : list of integers
    # @return an integer
    def findLIS(self, A):
        dp=[0]
        for i in A:
            if i>dp[-1]:
                dp.append(i)
            else:
                x=bs(dp,i)
                dp[x]=i
        return len(dp)-1