class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        tempStack = []
        for i, temp in enumerate(temperatures):
            while tempStack and tempStack[-1][0] < temp:
                day = tempStack.pop()
                res[day[1]] = i - day[1]
            tempStack.append((temp, i))
        return res