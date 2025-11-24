class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0
        if matrix[0][0] == '1':
            max_side = 1

        dp[0][0] = int(matrix[0][0])
        for i in range(1, cols):
            dp[0][i] = dp[0][i-1] + int(matrix[0][i])
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + int(matrix[i][0])
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + int(matrix[i][j])
        for i in range(0, rows):
            for j in range(0, cols):
                low = 1
                high = min(rows - i, cols - j)
                while low <= high:
                    mid = (low + high) // 2
                    total = dp[i + mid - 1][j + mid - 1]
                    if i > 0:
                        total -= dp[i - 1][j + mid - 1]
                    if j > 0:
                        total -= dp[i + mid - 1][j - 1]
                    if i > 0 and j > 0:
                        total += dp[i - 1][j - 1]
                    if total == mid * mid:
                        max_side = max(max_side, mid)
                        low = mid + 1
                    else:
                        high = mid - 1
        #         for m in range(i, rows):
        #             for n in range(j, cols):
        #                 if i == 0 and j == 0:
        #                     total = dp[m][n]
        #                 elif i == 0:
        #                     total = dp[m][n] - dp[m][j-1]
        #                 elif j == 0:
        #                     total = dp[m][n] - dp[i-1][n]
        #                 else:
        #                     total = dp[m][n] - dp[i-1][n] - dp[m][j-1] + dp[i-1][j-1]
        #                 if total == (m - i + 1) * (n - j + 1) and (m - i + 1) == (n - j + 1):
        #                     max_side = max(max_side, m - i + 1)
        #                 # print(i, j, m, n, total)
        # # print(dp)
        return max_side * max_side

a = Solution()
print(a.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))  # 4
print(a.maximalSquare([["0","1"],["1","0"]]))  # 1
print(a.maximalSquare([["0"]]))  # 0
print(a.maximalSquare([["1"]]))  # 1
print(a.maximalSquare([["0","1"],["1","0"]]))  # 1
print(a.maximalSquare([["0","1"]]))  # 1
print(a.maximalSquare([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]))  # 4
