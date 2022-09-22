# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        A =[ ]
        ans = dummy = head
        while head:
            A.append(head.val)
            head = head.next
        A = sorted(A)
        i =0
        while dummy:
            dummy.val = A[i]
            i+=1
            dummy = dummy.next
        return ans