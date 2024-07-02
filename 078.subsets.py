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
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums)+1):
            tmp = self.combine(len(nums),i)
            for j in tmp:
                res.append([nums[k-1] for k in j])
        return res
a = Solution()
print(a.subsets([4,5,6])) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]