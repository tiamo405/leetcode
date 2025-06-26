class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        total_amount = [0] * len(nums)
        total_amount[0] = nums[0]
        total_amount[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            total_amount[i] = max(total_amount[i - 1], total_amount[i - 2] + nums[i])
        return total_amount[-1]
a = Solution()
print(a.rob([1, 2, 3, 1]))  # Output: 4
print(a.rob([2, 7, 9, 3, 1]))  # Output: 12