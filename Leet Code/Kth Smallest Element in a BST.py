# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        A= []
        def allnum(root):
            if not root:
                return
            A.append(root.val)
            allnum(root.left)
            allnum(root.right)
        A = sorted(A)
        return A[k-1]