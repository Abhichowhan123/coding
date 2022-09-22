# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        d = root
        while d!=None:
            if d.val==val:
                break
            if d.val>val:
                d = d.left
            else:
                d = d.right
        return d
        # if root==None:
        #     return None
        # if root.val==val:
        #     return root
        # if root.val>val:
        #     return self.searchBST(root.left,val)
        # else:
        #     return self.searchBST(root.right,val)