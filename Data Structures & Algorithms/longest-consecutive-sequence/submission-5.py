class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        stor = set(nums)
        length = 0
        for i in range(len(nums)):
            if nums[i]-1 not in stor:
                longer = 0
                while nums[i] + longer in stor:
                    longer +=1
                    length = max(longer, length)
            else:
                continue
        return length
                

