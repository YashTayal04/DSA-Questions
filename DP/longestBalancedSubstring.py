class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, A):
        dp=[0]
        d={}
        d[']']='['
        d['}']='{'
        d[')']='('
        for i in range(1,len(A)):
            if A[i] not in d:
                dp.append(0)
            else:
                if d[A[i]]==A[i-1]:
                    l=2
                    if i>1:
                        l+=dp[i-2]
                    dp.append(l)
                elif dp[-1]>0:
                    if i-1-dp[i-1]>=0:
                        if d[A[i]]==A[i-1-dp[i-1]]:
                            l=dp[i-1]+2
                            if i-2-dp[i-1]>=0:
                                l+=dp[i-2-dp[i-1]]
                            dp.append(l)
                        else:
                            dp.append(0)
                    else:
                        dp.append(0)
                else:
                    dp.append(0)
        return max(dp)