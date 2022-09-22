# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def fla(root):
            if not root:
                return None
            lt = fla(root.left)
            rt = fla(root.right)
            if root.left:
                lt.right = root.right
                root.right = root.left
                root.left = None
            last = rt or lt or root
            return last
        fla(root)
