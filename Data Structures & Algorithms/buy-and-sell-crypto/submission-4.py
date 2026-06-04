class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        #sell = len(prices) -1
        res = 0
        for i in range(len(prices)):
            sell = prices[i]
            buy = min(buy,sell)
            if sell > buy:
                res = max(res,sell - buy)
        return res