# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        def absolute(root):
            if not root:
                return
            else:
                res.append(root.val)
                absolute(root.left)
                absolute(root.right)
        absolute(root)
        res.sort()
        mi = 99999999
        for i in range(len(res)-1):
            mi  =min(mi,abs(res[i]-res[i+1]))
        return mi
