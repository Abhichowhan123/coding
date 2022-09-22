# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        A = []
        def list(head):
            if not head:
                return
            A.append(head.val)
            list(head.next)
        list(head)
        def Bst(l,r):
            if l>r:
                return
            m = (l+r)//2
            root = TreeNode(A[m])
            root.left = Bst(l,m-1)
            root.right = Bst(m+1,r)
            return  root
        return  Bst(0,len(A)-1)
