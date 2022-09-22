# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = root.val
        def maxp(root):
            nonlocal m
            if not root:
                return 0
            lr = maxp(root.left)
            rr = maxp(root.right)
            curr_sum = max(lr, 0) + max(rr, 0) + root.val
            m = max(m,curr_sum)
            return root.val+max(lr,rr,0)
        maxp(root)
        return  m