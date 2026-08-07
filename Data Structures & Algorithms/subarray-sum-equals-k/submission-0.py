class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        prefixSum = {0: 1} # a empty sub array should be automatically accounted for

        for n in nums:
            currSum += n
            diff = currSum - k
            res += prefixSum.get(diff, 0) # if the prefix already exists, then we should add it to the result because that means there is prefixSum[diff] many ways to get that diff value
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        return res
