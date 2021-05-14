class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
        s=[]
        for i in A:
            if i!=')':
                s.append(i)
            else:
                c=0
                while s[-1]!='(':
                    c+=1
                    s.pop()
                if c<=2:
                    return 1
                s.pop()
                s.append('a')
        return 0