class Solution:
	# @param A : list of list of integers
	# @return an integer
	def adjacent(self, A):
        if len(A[0])==1:
            return max(A[0][0],A[1][0])
        dp=[max(A[0][0],A[1][0])]
        dp.append(max(dp[-1],max(A[0][1],A[1][1])))
        for i in range(2,len(A[0])):
            dp.append(max(dp[-1],dp[-2]+max(A[i])))
        return dp[-1]