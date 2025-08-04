class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        result = float('inf')
        left = 0
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                result = min(result, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return result if result != float('inf') else 0
a = Solution()
print(a.minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2
print(a.minSubArrayLen(4, [1,4,4]))  # Output: 1
print(a.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))