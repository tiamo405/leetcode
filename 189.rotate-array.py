class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return nums
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        return nums
a = Solution()
print(a.rotate([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]
print(a.rotate([-1, -100, 3, 99], 2))  # Output: [3, 99, -1, -100]
print(a.rotate([1, 2], 5))  # Output: [2, 1]