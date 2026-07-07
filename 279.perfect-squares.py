class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in squares[::-1]:
                if square <= i:
                    dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]

a = Solution()
print(a.numSquares(12))  # Output: 3 (4 + 4 + 4)
print(a.numSquares(13))  # Output: 2 (4 + 9)