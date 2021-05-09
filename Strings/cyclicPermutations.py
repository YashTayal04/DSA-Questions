class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        B=A+B+B[:-1]
        # print(B)
        n=len(B)
        z=[0]*n
        l=0
        r=0
        for i in range(1,n):
            if i>r:
                l=i
                r=i
                while r<n and B[r]==B[r-l]:
                    r+=1
                z[i]=(r-l)
                r-=1
            else:
                if i+z[i-l]<r:
                    z[i]=z[i-l]
                else:
                    l=i
                    while r<n and B[r]==B[r-l]:
                        r+=1
                    z[i]=(r-l)
                    r-=1
        c=0
        # print(z)
        x=len(A)
        for i in range(x,n):
            if z[i]>=x:
                c+=1 
        return c