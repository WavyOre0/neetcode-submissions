class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # solution trying to solve in log(n * m)
        # do binary search on the rows and then inside of the correct row
        top, bot = 0, len(matrix) - 1
        l,r = 0, len(matrix[0]) -1

        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][r] < target:
                top = mid + 1
            else:
                break
        if not top <= bot:
            return False
        row = (top + bot) // 2
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False
