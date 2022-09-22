# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dic = {}
        A = []
        def allnum(root):
            if not root:
                return
            A.append(root.val)
            allnum(root.left)
            allnum(root.right)
        allnum(root)
        A = sorted(A)
        a = 0
        for i in range(len(A)-1,-1,-1):
            a+=A[i]
            dic[A[i]]= a
        def convert(root):
            if not root:
                return
            root.val = dic[root.val]
            convert(root.left)
            convert(root.right)
        convert(root)
        return root
