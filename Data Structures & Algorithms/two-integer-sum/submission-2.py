class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        our_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in our_map:
                return [our_map[diff], i]
            our_map[n] = i
            

