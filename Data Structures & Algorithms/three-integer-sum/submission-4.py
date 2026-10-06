class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # -4,-1,-1,0,1,2
        # now that the numbers are in order we can search through the array for c
        for i,num in enumerate(nums):
            if i > 0 and nums == nums[i - 1]:
                continue
            l,r = i + 1, len(nums) -1
            while l < r:
                if num + nums[l] + nums[r] > 0:
                    r -= 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    if [num, nums[l], nums[r]] not in res:
                        res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l -1]:
                        l +=1
        return res
                    

        