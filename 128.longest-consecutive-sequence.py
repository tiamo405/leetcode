class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if not nums:
            return 0
        res, cnt = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                cnt += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                res = max(res, cnt)
                cnt = 1
        return max(res, cnt)
a = Solution()
print(a.longestConsecutive([])) # 4