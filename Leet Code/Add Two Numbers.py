# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

l1 = [2,4,3]
l2 = [5,6,4]
head = tempNode = ListNode(0)
carry = 0

while l1 or l2 or carry:
    if l1 or l2 or carry:
        if l1:
            carry+=(l1.val)
            l1 = l1.next
        if l2:
            carry += (l2.val)
            l2 = l2.next
    tempNode.val = carry%10
    carry = carry//10
    if l1 or l2 or carry:
        tempNode.next = ListNode(0)
        tempNode=tempNode.next
print(head)
