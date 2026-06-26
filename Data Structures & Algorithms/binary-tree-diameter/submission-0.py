# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0 # this makes if accessible in the recursion
        #return the height
        def dfs(curr) -> int:
            if not curr:
                return 0
            left = dfs(curr.left)
            right =  dfs(curr.right)
            
            self.result = max(self.result, right + left)
            return 1 + max(left, right)
        dfs(root)
        return self.result

