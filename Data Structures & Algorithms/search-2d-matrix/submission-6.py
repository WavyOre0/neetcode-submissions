class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowIndex = 0
        l,r = 0, len(matrix[0]) -1
        while l <= r and rowIndex < len(matrix):
            row = matrix[rowIndex]
            mid = (l + r) // 2
            if row[r] < target:
                rowIndex += 1
            elif row[mid] < target:
                l = mid + 1
            elif row[mid] > target:
                r = mid -1
            else:
                return True
        return False