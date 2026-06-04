class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        for r in range(k, len(nums)+1):
            window = sorted(nums[l:r])
            end = len(window) - 1
            res.append(window[end])
            l+=1
        return res
