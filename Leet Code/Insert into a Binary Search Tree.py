# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        d = TreeNode(val,None,None)
        def insert(root):
            if root.val>val:
                if root.left:
                    insert(root.left)
                else:
                    root.left = d
            elif root.val<val:
                if root.right:
                    insert(root.right)
                else:
                    root.right = d
        insert(root)
        return root