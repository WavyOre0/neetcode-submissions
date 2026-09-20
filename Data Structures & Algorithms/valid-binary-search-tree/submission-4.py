# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(currMin, currMax, node):
            if not node:
                return True
            if not (currMin < node.val < currMax):
                return False
            return dfs(currMin, node.val, node.left) and dfs(node.val, currMax, node.right)
        return dfs(float("-inf"), float("inf"), root)
