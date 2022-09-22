# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        A = []
        B = []
        def inorder1(root1):
            if not root1:
                return
            inorder1(root1.left)
            A.append(root1.val)
            inorder1(root1.right)
        def inorder2(root2):
            if not root2:
                return
            inorder2(root2.left)
            A.append(root2.val)
            inorder2(root2.right)
        inorder1(root1)
        inorder2(root2)
        A= sorted(A)
        return A