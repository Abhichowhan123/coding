# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_equal(left ,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return  left.val==right.val and  is_equal(left.left ,right.right) and is_equal(left.right ,right.left)

        is_equal(root.left ,root.right)
