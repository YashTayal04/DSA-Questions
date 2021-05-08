class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def smallestPrefix(self, A, B):
        ans=A[0]
        for i in A[1:]:
            if i<B[0]:
                ans+=i 
            else:
                break
        ans+=B[0]
        return ans