class Solution:
	# @param A : string
	# @return an integer
	def longestValidParentheses(self, A):
        dp=[0]
        ans=0
        for i in range(1,len(A)):
            if A[i]=='(':
                dp.append(0)
            else:
                x=dp[-1]
                y=i-x-1
                if y>=0:
                    if A[y]=='(':
                        x+=2
                        if y-1>=0:
                            x+=dp[y-1]
                        dp.append(x)
                        ans=max(ans,x)
                    else:
                        dp.append(0)
                else:
                    dp.append(0)
        # print(dp)
        return ans