# head = [2, 7, 4, 3, 5]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        A = []
        def findnum(head):
            if not head:
                return
            A.append(head.val)
            findnum(head.next)
        findnum(head)
        # A = [1,7,5,1,9,2,5,1]
        # A = [13,7,6,12,10]
        C = [0]*len(A)
        B = []
        for i in range(len(A)):
            if len(B)==0:
                B.append(i)
            else:
                if A[B[-1]]>A[i]:
                    B.append(i)
                else:
                    while  B and A[B[-1]]<A[i]:
                        C[B.pop()] = A[i]
                    B.append(i)
        print(C)