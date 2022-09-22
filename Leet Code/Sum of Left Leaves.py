# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        A = {0:0}
        def sum_leaves(root):
            if not root:
                return 0
            if root .left :
                if root.left.left==None and root.left.right ==None:
                    A[0]+=root.left.val
            sum_leaves(root.left)
            sum_leaves(root.right)
        sum_leaves(root)
        return A[0]