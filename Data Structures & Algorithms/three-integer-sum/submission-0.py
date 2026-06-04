class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if num == nums[i - 1] and i > 0:
                continue
            l = i+1
            r = len(nums) -1
            while l < r:
                if nums[l] + nums[r] + num > 0:
                    r -= 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l -1] and l < r:
                        l+=1
        return res
            
        # while i < j:
        #     if nums[i] == nums[i+1]:
        #         i += 1
        #     elif -(nums[i] + nums[j]) in storage and storage.get(-(nums[i] + nums[j]), 0) > 0:
        #         res.append([nums[i],nums[j], -(nums[i]+nums[j])])
        #         storage[-(nums[i] + nums[j])] -= 1
        #     else:
        #         j-=1
        # return res