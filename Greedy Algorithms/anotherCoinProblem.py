class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans=0
        c=1
        while A>c:
            c*=5
        while A>0:
            ans+=A//c
            A=A%c
            c//=5
        return ans