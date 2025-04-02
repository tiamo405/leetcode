class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i-1])
        return max_gap
a = Solution()
print(a.maximumGap([3,6,9,1])) # 3
print(a.maximumGap([10])) # 0