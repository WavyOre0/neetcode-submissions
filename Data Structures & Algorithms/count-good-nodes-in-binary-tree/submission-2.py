# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(prev, node):
            if not node:
                return 0
            if node.val >= prev:
                return 1 + dfs(node.val, node.left) + dfs(node.val, node.right)
            else:
                return dfs(prev, node.left) + dfs(prev, node.right)
        return dfs(root.val, root)