class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        f=0
        for i in range(len(A)//2):
            if A[i]!=A[-1-i]:
                f+=1
        if f==1 or (f==0 and len(A)%2==1):
            return "YES"
        else:
            return "NO"
