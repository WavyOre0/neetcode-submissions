class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # should work similar to unique paths I\
        # instead of creating each row ourselves, we can update it inside of the obstacleGrid
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        #row = [1] * n
        dp = [0] * n
        dp[n - 1] = 1
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < n:
                    dp[c] = dp[c] + dp[c + 1]
                else:
                    dp[c] = dp[c]
        return dp[0]