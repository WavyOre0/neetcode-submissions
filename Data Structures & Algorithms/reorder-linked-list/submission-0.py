# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1, l2 = head, head.next
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
        # Now l1 is at the middle of head
        #Trying to reverse the second half of the list
        curr = l1.next  
        prev = l1.next = None # You want to initalize this to either l1.next or None
        while curr:
            newNode = curr.next
            curr.next = prev
            prev = curr
            curr = newNode
        p1,p2 = head, prev # need to have two pointers to 
        while p2:
            # return None
            curr = p1.next
            curr2 = p2.next
            p1.next = p2
            p2.next = curr
            
            p2 = curr2
            p1 = curr
        

