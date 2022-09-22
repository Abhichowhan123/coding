"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = []
        queue.append(root)
        depth = 0
        while queue:

            for i in range(len(queue)):
                node = queue.pop(1)
                if node.children:
                    for j in node.children:
                        queue.append(j)
            depth+=1