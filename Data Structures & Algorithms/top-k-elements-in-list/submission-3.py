class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            result[num] = 1 + result.get(num, 0)
        
        for num, count in result.items():
            freq[count].append(num)        
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        