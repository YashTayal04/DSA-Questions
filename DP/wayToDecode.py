class Solution:
	# @param A : string
	# @return an integer
	def numDecodings(self, A):
	    if int(A[0])==0:
	        return 0
        ways=[1,1]
        if len(A)==1:
            return ways[1]
        else:
            for i in range(1,len(A)):
                x=0
                if int(A[i])!=0:
                    x+=ways[-1]
                if int(A[i-1:i+1])<=26 and int(A[i-1])!=0:
                    x+=ways[-2]
                if x==0:
                    return 0
                ways.append(x%1000000007)
            return ways[-1]