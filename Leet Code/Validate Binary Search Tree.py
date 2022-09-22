class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        A = []
        def isvalid(root):
            if not root:
                return
            isvalid(root.left)
            A.append(root.val)
            isvalid(root.right)
        isvalid(root)
        for i in range(len(A)-1):
            if A[i] >=A[i+1]:
                return False
        return True
