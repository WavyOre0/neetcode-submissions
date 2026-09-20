# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # This solution doesnt work on leetcode
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            l = len(queue)
            #node = queue.popleft()
            for i in range(l):
                print(l)
                node = queue.popleft()
                if i == 0 and node:
                    res.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                
        return res

