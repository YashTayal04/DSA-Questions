class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):
        al=0
        ar=0
        n=len(A)
        for i in range(len(A)):
            l=i-1
            r=i+1
            while l>=0 and r<n:
                if A[l]==A[r]:
                    if r-l>ar-al:
                        al=l
                        ar=r
                    l-=1
                    r+=1
                else:
                    break
            l=i
            r=i+1
            while l>=0 and r<n:
                if A[l]==A[r]:
                    if r-l>ar-al:
                        al=l
                        ar=r
                    l-=1
                    r+=1
                else:
                    break
        return A[al:ar+1]