# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # just use two pointers, the further pointer should 
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        temp = head
        for i in range(length - n):
            temp = temp.next
        node = head
        dummy = ListNode(0, head)
        prev = dummy
        while node:
            if node == temp:
                prev.next = temp.next
                node = prev.next
                return dummy.next
            else:
                prev = prev.next
                node = node.next
