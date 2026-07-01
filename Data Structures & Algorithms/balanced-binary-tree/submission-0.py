# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(curr):
            if not curr:
                return [True, 0]
            hL =  dfs(curr.left)
            hR =  dfs(curr.right)
            balanced = abs(hR[1] - hL[1]) <= 1 and hL[0] and hR[0]
            return [balanced, 1 + max(hR[1], hL[1])]
        diff = dfs(root)
        return diff[0]