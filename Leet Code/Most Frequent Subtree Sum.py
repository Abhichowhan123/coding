# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        A = {}
        total = 0
        def frequent(root):
            nonlocal A
            nonlocal total
            if not root:
                return 0
            lr = frequent(root.left)
            rr = frequent(root.right)
            total = root.val+lr+rr

            if total not in A:
                A[total] = 1
            else:
                A[total]+=1
            return total
        frequent(root)
        A =sorted(A.items(),key = lambda x:x[1],reverse= True)
        B = []
        s = A[0][1]
        for i,j in A:
            if s==j:
                B.append(i)
            else:
                break
        return B

