class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output should be an array
        res = []
        # output[i] % nums[i] != 0
        i = 0
        while i < len(nums):
            val = 1
            for num in range(len(nums)):
                if num == i:
                    continue
                val *= nums[num]
            res.append(val)
            i+=1
            
        return res