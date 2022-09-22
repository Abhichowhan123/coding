# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        cur = -999999999999
        c = -999999999999
        fist = -999999999999
        midd =-999999999999
        last = -999999999999
        def checK(root):
            if not root:
                return
            nonlocal fist,midd,last,cur,c
            checK(root.left )
            if root.val>cur:
                cur = root.val
                c = root
            else:
                if fist==-999999999:
                    fist =c
                    midd = root
                else:
                    last  =root
                    fist.val,last.val = last.val,fist.val
            checK(root.right)
        checK(root)
        if last==-999999999:
            fist.val,midd.val = midd.val,fist.val


