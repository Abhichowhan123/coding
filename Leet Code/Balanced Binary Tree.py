# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            return max(lh,rh)+1
        def isBal(root):
            if not root:
                return True
            if isBal(root.left)==False:
                return False
            if isBal(root.right)==False:
                return False
            lh = height(root.left)
            rh = height(root.right)
            if abs(lh - rh)<=1:
                return True
            else:
                return False
        return(isBal(root))