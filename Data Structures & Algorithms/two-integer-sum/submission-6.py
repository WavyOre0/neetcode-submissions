class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        our_map = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in our_map:
                return [our_map[diff], i]
            our_map[nums[i]] = i


