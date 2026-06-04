# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # check if each list is empty
        if not list1:
            return list2
        if not list2:
            return list1
        # have a pointer to each list, and only move the pointer that has a value less than the other
        ptr1 = list1
        ptr2 = list2
        # ptr to output
        res = ListNode()
        tail = res
        while ptr1 and ptr2:
            if ptr1.val >= ptr2.val:
                tail.next = ptr2
                ptr2 = ptr2.next
            else:
                tail.next = ptr1
                ptr1 = ptr1.next
            tail = tail.next
        if ptr1:
            tail.next = ptr1
            
        if ptr2:
            tail.next = ptr2
        return res.next