# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        A = []
        queue = []
        queue.append(root)
        while queue:
            qlen = len(queue)
            level = []
            for i in range(qlen):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                if level:
                    if len(A)>0:
                        A.pop()
                        A.append(level)
                    else:
                        A.append(level)
        return(A[0][0])
