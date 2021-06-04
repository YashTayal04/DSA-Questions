class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        d={}
        for i in range(len(A)):
            if A[i] in d:
                d[A[i]].append(i)
            else:
                d[A[i]]=[i]
        sub={}
        for i in range(2,len(A)):
            for j in range(i):
                if 2*A[j]-A[i] in d:
                    x=0
                    for k in d[2*A[j]-A[i]]:
                        if k<j:
                            if (k,j) in sub:
                                x+=sub[(k,j)]
                            x+=1
                    if x>0:
                        sub[(j,i)]=x
        # print(sub)
        return sum(sub.values())