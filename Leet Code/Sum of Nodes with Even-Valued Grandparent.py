# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        A = 0
        if root:
            if root.val%2==0 and (root.left or root.right):
                if root.left != None and (root.left.left or root.left.right):
                    A+=root.left.left.val if root.left.left else 0
                    A += root.left.right.val if root.left.right else 0

                if root.right!=None and (root.right.left or root.right.right):
                    A += root.right.left.val if root.right.left else 0
                    A += root.right.right.val if root.right.right else 0
            return A+self.sumEvenGrandparent(root.left)+self.sumEvenGrandparent(root.right)
        return A
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     A = {0:0}
#     def sumEvenGrandparent(self, root: TreeNode) -> int:
#         if root:
#             if root.val%2==0 :
#                 if root.left!=None :
#                     if root.left.left!=None:
#                         self.A[0]+=root.left.left.val
#                     if root.left.right!=None:
#                         self.A[0]+=root.left.right.val
#                 if root.right!=None :
#                     if root.right.left!=None:
#                         self.A[0]+=root.right.left.val
#                     if root.right.right!=None:
#                         self.A[0]+=root.right.right.val
#             self.sumEvenGrandparent(root.left)
#             self.sumEvenGrandparent(root.right)
#         return self.A[0]