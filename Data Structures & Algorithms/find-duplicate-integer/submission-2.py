class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # solution to just solve, not do the follow up
        stor = {}
        for c in nums:
            stor[c] = 1 + stor.get(c, 0)
            if stor[c] > 1:
                return c
