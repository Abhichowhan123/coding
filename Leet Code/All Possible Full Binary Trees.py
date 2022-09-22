# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        A= {0:[],1:[TreeNode()]}

        def possicle (n):
            if n in A:
                return A[n]
            result = []
            for l in range(n):
                r  =n-1-l
                lt = possicle(l)
                rt = possicle(r)
                for t1 in lt:
                    for t2 in rt:
                        result.append(TreeNode(0,t1,t2))
            A[n] = result
            return result
        return possicle(n)
