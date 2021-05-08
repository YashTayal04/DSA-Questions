class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        c=0
        for i in A:
            if i=='a':
                c+=1 
        return c*(c+1)//2