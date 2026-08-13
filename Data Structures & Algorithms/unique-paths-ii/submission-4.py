class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #Brute Force DFS version
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        bank = {(m - 1, n - 1): 1}
        def dfs(r, c):
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0
            if (r,c) in bank:
                return bank[r, c] 
            bank[(r, c)] =  dfs( r + 1, c) + dfs( r , c + 1)
            return bank[(r, c)]
        return dfs(0, 0)