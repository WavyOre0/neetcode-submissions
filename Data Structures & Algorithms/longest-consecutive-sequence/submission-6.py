class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for i in range(len(nums)):
            #seen.add(nums[i])
            if nums[i] - 1 not in seen:
                length = 0
                
                while nums[i] + length in seen:
                    length += 1
                    res = max(length, res)
        return res