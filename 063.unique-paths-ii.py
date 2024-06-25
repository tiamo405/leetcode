class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dq = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dq[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dq[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dq[i][j] = 0
                else:
                    dq[i][j] = dq[i-1][j] + dq[i][j-1]
        return dq[-1][-1]
a = Solution()
print(a.uniquePathsWithObstacles([[0,1],[0,0]])) # 1