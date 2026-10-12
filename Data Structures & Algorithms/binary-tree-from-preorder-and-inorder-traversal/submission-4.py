# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # the first node in preorder is the root
        # find that node in the inorder list and you can see that it is blocking off the left and right side
        pre_indx = {val: indx for indx, val in enumerate(inorder)}

        #dummy = TreeNode(0)
        q = deque(preorder)
        self.pre = 0
        def build(low, high):
            if low == high:
                return None
            if q:
                node = q.popleft()
                root = TreeNode(node)
                mid = pre_indx[node]
                root.left = build(low, mid)
                root.right = build(mid + 1, high)
                return root
        return build(0, len(preorder))
            

            