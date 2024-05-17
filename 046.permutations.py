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
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permutations(nums)

    
a = Solution()
print(a.permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]