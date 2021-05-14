class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        l1=[]
        l2=[]
        for i in A:
            while len(l1)>0 and l1[-1]>i:
                l2.append(l1.pop())
            l1.append(i)
            while len(l2)>0:
                l1.append(l2.pop())
        return l1