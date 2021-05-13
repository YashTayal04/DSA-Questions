class Solution:
	# @param A : list of integers
	# @return an integer
	def candy(self, A):
        c=[1 for i in range(len(A))]
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                c[i]=c[i-1]+1
        for i in range(len(A)-2,-1,-1):
            if A[i]>A[i+1]:
                c[i]=max(c[i],c[i+1]+1)
        return sum(c)