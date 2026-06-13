class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.stor = {}
        self.cap = capacity # key = nodes
        self.left, self.right = Node(0,0), Node(0, 0)
        self.left.next = self.right # Left = LRU
        self.right.prev = self.left # Right = Most recent
    def remove(self, node):
        # remove from list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def insert(self, node):
        # insert at right
        prev = self.right.prev 
        self.right.prev = node
        prev.next = node
        node.prev = prev
        node.next = self.right
        
    def get(self, key: int) -> int:
        if key in self.stor:
            self.remove(self.stor[key])
            self.insert(self.stor[key])
            return self.stor[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.stor:
            self.remove(self.stor[key])
        self.stor[key] = Node(key, value)
        self.insert(self.stor[key])

        if len(self.stor) > self.cap:
            # handling 
            lru = self.left.next
            self.remove(lru)
            del self.stor[lru.key]

