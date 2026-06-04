"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {None: None} # None: None just initalizes it to be None automatically rather than just empty
        if not head:
            return head
        tmp = head
        while tmp:
            hmap[tmp] = Node(tmp.val)
            tmp = tmp.next
        newHead = hmap.get(head)
        curr = head
        while newHead:
            newHead.next = hmap.get(curr.next)
            newHead.random = hmap.get(curr.random)
            newHead = hmap.get(curr.next)
            curr = curr.next
        return hmap[head]
        