class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        le=list(A[::-1])
        # print(le)
        l=0
        r=0
        a=""
        while r<len(le):
            if le[r]!=" ":
                r+=1 
            elif l==r:
                l+=1 
                r+=1 
            else:
                x=r 
                if len(a)!=0:
                    a+=" "
                r-=1
                while l<=r:
                    a+=le[r]
                    r-=1 
                l=x+1
                r=x+1
        r-=1
        if len(a)!=0 and l<=r:
            a+=" "
        while l<=r:
            a+=le[r]
            r-=1 
        return a