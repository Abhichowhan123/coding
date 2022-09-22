# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        rec = []
        q= deque()
        q.append(root)
        while q:
            qlen=len(q)
            level = []
            for i in range(qlen):
                n = q.popleft()
                if n:
                    level.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if level:
                rec.append(level)
        total = rec[len(rec)-1]
        a = 0
        for i in range(len(total)):
            a+=total[i]
        return a