class Solution:
	# @param A : string
	# @return an integer
	def minCut(self, A):
        pa=[[0 for i in range(len(A))] for i in range(len(A))]
        for k in range(1,len(A)+1):
            for i in range(len(A)-k+1):
                if k==1:
                    pa[i][i]=1
                elif k==2:
                    if A[i]==A[i+1]:
                        pa[i][i+1]=1
                else:
                    j=i+k-1
                    if A[i]==A[j] and pa[i+1][j-1]==1:
                        pa[i][j]=1
        # print(pa)
        dp=[i for i in range(len(A))]
        for i in range(1,len(A)):
            if pa[0][i]==1:
                dp[i]=0
            for j in range(1,i+1):
                if pa[j][i]==1:
                    dp[i]=min(dp[i],dp[j-1]+1)
        # print(dp)
        return dp[-1]
                