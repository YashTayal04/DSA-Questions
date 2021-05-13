class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        l=[(B[i],A[i]) for i in range(len(A))]
        l.sort()
        e=0
        ans=0
        for i in l:
            if i[1]>=e:
                ans+=1
                e=i[0]
        return ans