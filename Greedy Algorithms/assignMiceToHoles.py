class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def mice(self, A, B):
        A.sort()
        B.sort()
        ans=0
        for i in range(len(A)):
            ans=max(ans,abs(B[i]-A[i]))
        return ans