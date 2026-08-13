class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # start with bottom row
        # intuition is to start from bottom and do right + down to get the value of possible moves from the position you are at
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1 , -1):# we know last column will only have 1's so no need to handle that condition
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]