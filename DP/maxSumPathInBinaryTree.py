# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
ans=-100000
def helper(A):
    global ans
    if A==None:
        return 0
    left=max(0,helper(A.left))
    right=max(0,helper(A.right))
    ans=max(ans,A.val+left+right)
    return max(left,right)+A.val
class Solution:
	# @param A : root node of tree
	# @return an integer
	def maxPathSum(self, A):
	    global ans
	    ans=-100000
	    helper(A)
	    return ans
        