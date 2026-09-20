# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []
        
        l = 1 # use to keep track of the size of the level
        while queue:
            l = len(queue)
            inner = []
            for i in range(l):
                curr = queue.popleft()
                if curr:
                    inner.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if inner:
                res.append(inner)
        return res

