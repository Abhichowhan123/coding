# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    a = 0
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def gettarget(o,c,t):
            if not o:
                return
            if o==t:
                self.a= c
            gettarget(o.left,c.left,t)
            gettarget(o.right, c.right, t)
            return self.a
        gettarget(original, cloned, target)
        return self.a