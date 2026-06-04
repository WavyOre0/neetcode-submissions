class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = hours
        # piles[i] = # of banans in that pile
        # the upperbound for k should always be the largest in piles
        l,r = 1, max(piles) # pointers to the possible values of k
        res = r
        while l <=r:
            k = (l + r) // 2
            hours = 0 # a way to calculate the hours taken for each # in search
            for p in piles:
                hours += math.ceil((p / k))
            if hours <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
        return res




