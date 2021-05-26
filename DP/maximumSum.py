class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        dp=[(A[0]*B,A[0]*(B+C),A[0]*(B+C+D))]
        for i in range(1,len(A)):
            dp.append([0,0,0])
            dp[-1][0]=max(dp[-2][0],A[i]*B)
            dp[-1][1]=max(dp[-2][1],dp[-1][0]+A[i]*C)
            dp[-1][2]=max(dp[-2][2],dp[-1][1]+A[i]*D)
        return dp[-1][2]

        