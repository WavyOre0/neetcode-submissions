class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        w = len(heights) -1
        while i < w:
            h = min(heights[i], heights[w])
            width = w - i
            res = max(res, h * width)
            if h == heights[w]:
                w -=1
            else:
                i += 1
        return res