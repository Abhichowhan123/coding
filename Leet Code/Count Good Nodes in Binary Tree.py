# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_Good_Nodes(root,m):
            if root==None:
                return 0
            r =1 if root.val>=m else 0
            m = max(m,root.val)
            r+=count_Good_Nodes(root.left,m )
            r+=count_Good_Nodes(root.right,m)
            return r
        return count_Good_Nodes(root,root.val)
