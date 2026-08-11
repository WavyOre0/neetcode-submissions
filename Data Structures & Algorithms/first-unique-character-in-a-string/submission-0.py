class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = defaultdict(int)
        for c in s:
            hmap[c] += 1
        for i,c in enumerate(s):
            if hmap[c] == 1:
                return i
        return -1