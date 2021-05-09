class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n=len(A)
        z=[n]*n
        l=0
        r=0
        for i in range(1,n):
            if i>r:
                l=i
                r=i
                while r<n and A[r]==A[r-l]:
                    r+=1
                z[i]=(r-l)
                r-=1
            else:
                if i+z[i-l]<=r:
                    z[i]=z[i-l]
                else:
                    l=i
                    while r<n and A[r]==A[r-l]:
                        r+=1
                    z[i]=(r-l)
                    r-=1
            if i+z[i]==n:
                return i
        return n
        
        
        
        