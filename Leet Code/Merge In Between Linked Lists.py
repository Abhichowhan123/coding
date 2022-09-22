list1 = [0,1,2,3,4,5,6]
a = 2
b = 5
list2 = [1000000,1000001,1000002,1000003,1000004]
# [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = cur = list1
        for i in range(a - 1):
            cur = cur.next

        A = cur
        for i in range(b - a + 2):
            A = A.next

        t = list2
        while t.next:
            t = t.next

        cur.next = list2
        t.next = A
        return head

