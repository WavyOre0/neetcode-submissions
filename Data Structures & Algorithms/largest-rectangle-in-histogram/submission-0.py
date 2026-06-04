class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # You want to be able to access the index the height starts at
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop() #[7,1]
                maxArea = max(maxArea, height * (i - index)) # The index 
                start = index
            stack.append((start, h))
        # Now check for when the stack contains heights that reach the end
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea