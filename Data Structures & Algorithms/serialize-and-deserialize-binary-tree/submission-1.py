# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "a-"

        res = ""
        res += str(root.val) + '-'
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res

        # q = deque()
        # res = ""
        # q.append(root)
        # while q:
        #     node = q.popleft()
        #     if not node:
        #         res += "a-"
        #     else:
        #         q.append(node.left)
        #         q.append(node.right)
        #         res += str(node.val) + '-'
        # return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        vals = data.split('-')
        #print(data)
        def solve():
            if self.i >= len(vals) - 1 or vals[self.i] == 'a':
                return None
                    
            root = TreeNode(int(vals[self.i]))
            self.i += 1
            root.left = solve()
            self.i += 1
            root.right = solve()
            
            return root
        return solve()
                    