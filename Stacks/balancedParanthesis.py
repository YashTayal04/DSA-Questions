class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):
        l=[]
        d={')':'(', '}':'{',']':'['}
        for i in A:
            if i in d:
                if len(l)>0 and l[-1]==d[i]:
                    l.pop()
                else:
                    return 0
            else:
                l.append(i)
        if len(l)>0:
            return 0
        else:
            return 1