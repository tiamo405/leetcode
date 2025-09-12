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
        def rob_linear(houses):
            rob = [0] * len(houses)
            rob[0] = houses[0]
            rob[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                rob[i] = max(rob[i-1], rob[i-2] + houses[i])
            return rob[-1]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
a = Solution()
print(a.rob([2,3,2]))  # Output: 3
print(a.rob([1,2,3,1]))  # Output: 4
print(a.rob([1,2,3]))  # Output: 3
print(a.rob([1,1,1,2]))  # Output: 3
print(a.rob([1,3,6,7,10,7,1,8,5,9,1,4,4,3]))  # Output: 41