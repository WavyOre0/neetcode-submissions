class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            midRow = (top + bottom) // 2 # 1
            if matrix[midRow][0] > target:
                bottom = midRow - 1
            elif matrix[midRow][r] < target:
                top = midRow + 1
            else:
                break
        if not top <= bottom:
            return False
        row = (top + bottom) // 2
        while l <= r:
            mid = (l + r) // 2    
            if matrix[row][mid] == target:
                return True                      
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
                    