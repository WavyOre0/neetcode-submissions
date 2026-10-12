# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        # need to only split once at a node and never again anywhere down the node
        # with that in mind I need a boolean so I can remember if I split already
        #return from this function max path sum without splitting
        def solve(root):
            if not root:
                return 0
            left = solve(root.left)
            right = solve(root.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)
            #compute max path sum with a split
            res[0] = max(root.val + leftMax + rightMax, res[0])
            return root.val + max(leftMax, rightMax)
        solve(root)
        return res[0]
