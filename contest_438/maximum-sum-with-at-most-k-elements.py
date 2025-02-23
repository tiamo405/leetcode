class Solution(object):
    def maxSum(self, grid, limits, k):
        """
        :type grid: List[List[int]]
        :type limits: List[int]
        :type k: int
        :rtype: int
        """
        # ©leetcode
        n, m = len(grid), len(grid[0])
        res = 0
        # sort theo tung hang cua  grid
        for i in range(n):
            grid[i].sort()
        while k > 0:
            max_val = -1e9
            max_index = -1
            for i in range(n):
                if limits[i] == 0:
                    continue
                if max_val < grid[i][-1]:
                    max_val = grid[i][-1]
                    max_index = i
            res += max_val
            limits[max_index] -= 1
            k -= 1
            grid[max_index].pop()
        return res

a = Solution()
print(a.maxSum([[5,3,7],[8,2,6]], [2,2], 3))