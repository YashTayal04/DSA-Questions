def helper(m,A):
    ans=0
    l=m-1 
    for i in range(m-1,-1,-1):
        if A[i]=='x':
            ans+=(l-i)
            l-=1
    r=m+1
    for i in range(m+1,len(A)):
        if A[i]=='x':
            ans+=(i-r)
            r+=1
    return ans

class Solution:
	# @param A : string
	# @return an integer
	def seats(self, A):
        c=A.count('x')
        if c<=1:
            return 0
        elif c%2==1:
            t=0
            for i in range(len(A)):
                if A[i]=='x':
                    t+=1 
                    if t==c//2 + 1:
                        return helper(i,A)%10000003
        else:
            ans=len(A)**2
            t=0
            for i in range(len(A)):
                if A[i]=='x':
                    t+=1 
                    if t==c//2 :
                        ans=helper(i,A)
                    elif t==c//2 + 1:
                        return min(ans,helper(i,A))%10000003