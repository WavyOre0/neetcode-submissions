class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = innerSub = 0
        res = float('inf')
        for r in range(len(nums)):
            innerSub += nums[r]
            while innerSub >= target:
                res = min(res, r-l + 1)
                innerSub -= nums[l]
                l += 1

        return 0 if res == float('inf') else res
            

            
