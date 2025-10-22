class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        arrs = []
        self.dfs(k, n, 1, [], arrs)
        return arrs

    def dfs(self, k, n, start, path, arrs):
        if k == 0 and n == 0:
            arrs.append(path)
            return
        for i in range(start, 10):
            if i > n:
                break
            self.dfs(k - 1, n - i, i + 1, path + [i], arrs)
a = Solution()
print(a.combinationSum3(3, 7))
print(a.combinationSum3(3, 9))