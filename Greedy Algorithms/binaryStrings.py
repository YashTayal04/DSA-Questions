class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        a=[0 for i in range(len(A))]
        c=0
        ans=0
        for i in range(len(A)):
            c+=a[i]
            if (c%2==0 and A[i]=='1') or (c%2==1 and A[i]=='0'):
                pass
            else:    
                if i+B>len(A):
                    return -1
                else:
                    ans+=1 
                    c+=1 
                    if i+B<len(A):
                        a[i+B]-=1 
        return ans