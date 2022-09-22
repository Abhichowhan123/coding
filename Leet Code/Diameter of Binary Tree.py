# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.maxi=0
        def height(root):
            if not root:
                return 0
            lh=height(root.left)
            rh=height(root.right)
            self.maxi=max(self.maxi,lh+rh)
            return 1+max(lh,rh)
        height(root)
        return self.maxi

