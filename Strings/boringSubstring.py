class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        a=list(A)
        l=0
        r=len(a)-1
        while l<=r:
            if ord(a[l])%2==0:
                a[l],a[r]=a[r],a[l]
                r-=1
            else:
                l+=1 
        # print(a,l)
        if l==0 or r==len(a)-1:
            return 1
        else:
            minl=a[0]
            maxl=a[0]
            for i in range(l):
                minl=min(minl,a[i])
                maxl=max(maxl,a[i])
            minr=a[l]
            maxr=a[l]
            for i in range(l,len(a)):
                minr=min(minr,a[i])
                maxr=max(maxr,a[i])
            if abs(ord(maxl)-ord(minr))!=1 or abs(ord(maxr)-ord(minl))!=1:
                return 1
            else:
                return 0
