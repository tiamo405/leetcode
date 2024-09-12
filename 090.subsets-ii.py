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
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        for i in range(len(nums)+1):
            tmp = self.combine(len(nums),i)
            for j in tmp:
                res.append([nums[k-1] for k in j])
        tmp = []
        for i in res:
            i.sort()
            if i not in tmp:
                tmp.append(i)
        return tmp
a = Solution()
print(a.subsetsWithDup([1,2,2]))