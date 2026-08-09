class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r = 0 ,len(matrix) - 1

        while l <= r:
            for i in range(r - l):
                top, bottom = l , r 
                # make temp
                tmp = matrix[top][l + i]
                #update top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # update bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                #update bottom right
                matrix[bottom][r - i]  = matrix[top + i][r]
                # update top right:
                matrix[top + i][r] = tmp
            r -= 1
            l += 1