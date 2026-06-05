# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        A, B = l1, l2
        dummy = ListNode()
        curr = dummy
        carry = 0
        # I want to change B to the output.
        while A or B:
            v1 = A.val if A else 0
            v2 = B.val if B else 0
            total = v1 + v2 + carry

            if total >= 10:
                t2 = total % 10
                carry = total // 10
                curr.val = t2
            else:
                curr.val = total
                carry = 0
            A = A.next if A else None
            B = B.next if B else None
            curr.next = ListNode(carry)
            if not A and not B and carry == 0:
                curr.next = None
            curr = curr.next
        return dummy