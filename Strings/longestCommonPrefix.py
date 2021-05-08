class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
	    if len(A)==1:
	        return A[0]
        ans=""
        for i in range(1000000):
            f=0
            if len(A[0])<=i:
                break
            for j in range(1,len(A)):
                if len(A[j])<=i or (A[0][i]!=A[j][i]) :
                    f=1 
                    break
            if f==1:
                break
            else:
                ans+=A[0][i]
        return ans