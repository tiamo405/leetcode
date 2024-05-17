class Solution(object):
    def permutations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]  
        perms = []
        for i in range(len(nums)):
            for perm in self.permutations(nums[:i] + nums[i+1:]):
                perms.append([nums[i]] + perm)
        return perms

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        arr = [i for i in range(n)]
        res = []
        for i in self.permutations(arr):
            tmp = []
            for j in i:
                tmp.append(nums[j])
            if tmp not in res:
                res.append(tmp)
        return res

a = Solution()
print(a.premuteUnique([1,1,2])) # [[1,1,2],[1,2,1],[2,1,1]]
    