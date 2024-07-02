class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(start, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(start, n+1):
                backtrack(i+1, path+[i])
        backtrack(1, [])
        return res
a = Solution()
print(a.combine(4,2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]