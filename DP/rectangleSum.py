class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        for i in range(len(A)):
            for j in range(1,len(A[0])):
                A[i][j]+=A[i][j-1]
        ans=0
        for i in range(len(A[0])):
            for j in range(i,len(A[0])):
                c=0
                for k in range(len(A)):
                    c+=A[k][j]
                    if i>0:
                        c-=A[k][i-1]
                    c=max(0,c)
                    ans=max(ans,c)
        return ans