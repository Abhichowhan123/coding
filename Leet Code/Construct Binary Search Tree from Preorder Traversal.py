class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        cur = 0

        def dfs(low, high):
            nonlocal cur
            if cur >= len(preorder):
                return None
            if not (preorder[cur] > low and preorder[cur] < high):
                return None
            root = TreeNode(preorder[cur])
            cur += 1
            root.left = dfs(low, root.val)
            root.right = dfs(root.val, high)
            return root

        return dfs(float("-inf"), float("inf"))