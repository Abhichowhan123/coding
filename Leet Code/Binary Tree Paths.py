# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        A = []
        def binary(root, s):
            if not root:
                return
            if not root.left and not root.right:
                A.append(s)
                return
            if root.left:
                binary(root.left,s+f"->{root.left.val}")
            if root.right:
                binary(root.right,s+f"->{root.right.val}")
        binary(root,f"{root.val}")
        return A