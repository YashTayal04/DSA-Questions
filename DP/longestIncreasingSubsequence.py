class Solution:
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):
        dp=[(1,0)]
        for i in range(1,len(A)):
            l=1
            ind=i 
            for j in range(i):
                if A[i]>A[j] and dp[j][0]+1>l:
                    l=dp[j][0]+1
                    ind=j
            dp.append((l,ind))
        l=1
        ind=0
        for i in range(1,len(A)):
            if dp[i][0]>l:
                l=dp[i][0]
                ind=i 
        return l
        # ans=[A[ind]]
        # while dp[ind][1]!=ind:
        #     ind=dp[ind][1]
        #     ans.append(A[ind])
        # return ans[::-1]