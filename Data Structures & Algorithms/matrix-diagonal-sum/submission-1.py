class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        #l,r = 0, len(mat) - 1
        #seen = set()
        for i in range(len(mat)):
            r = len(mat) - 1 - i
            #seen.add((i,i))
            res += mat[i][i]
            if r != i:
                res += mat[i][r]      
        
        return res