class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dq = [[0 for i in range(n)] for j in range(m)]
        dq[0][0] = grid[0][0]
        for i in range(1, m):
            dq[i][0] = dq[i-1][0] + grid[i][0]
        for i in range(1, n):
            dq[0][i] = dq[0][i-1] + grid[0][i]
        for i in range (1, m):
            for j in range(1, n):
                dq[i][j] = min(dq[i-1][j], dq[i][j-1]) + grid[i][j] 
        return dq[-1][-1]
a = Solution()
print(a.minPathSum([[1,2,3],[4,5,6]]))