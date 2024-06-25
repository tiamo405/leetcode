class Solution(object):
    def uniquePaths(self, m, n):
        dq = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dq[i][0] = 1
        for i in range(n):
            dq[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dq[i][j] = dq[i-1][j] + dq[i][j-1]
        return dq[m-1][n-1]
a = Solution()
print(a.uniquePaths(3, 7)) # 28