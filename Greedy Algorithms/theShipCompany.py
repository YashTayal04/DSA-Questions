class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        C.sort()
        mi=0
        temp=A
        for i in C:
            if i<=temp:
                mi+=(i*(i+1)//2)
                temp-=i
            else:
                mi+=(i*(i+1)//2)
                i-=temp
                mi-=(i*(i+1)//2)
                break
        ma=0
        for i in range(A):
            for j in range(B-1,-1,-1):
                if j==0:
                    ma+=C[j]
                    C[j]-=1
                    break
                elif C[j]>C[j-1]:
                    ma+=C[j]
                    C[j]-=1
                    break
        return [ma,mi]
                
            