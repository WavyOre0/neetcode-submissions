class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if stack and temperatures[stack[-1]] > temperatures[i]:
                stack.append(i) # [1, 2, 3, 4]
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    top = stack.pop()
                    res[top] = i - top
                stack.append(i)

        return res
            

