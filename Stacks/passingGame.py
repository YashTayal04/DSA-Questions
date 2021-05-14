class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        l=[B]
        for i in C:
            if i==0:
                l.pop()
            else:
                l.append(i)
        return l[-1]