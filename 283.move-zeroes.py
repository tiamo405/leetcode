class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index_zero_first = 0
        if nums[0] == 0:
            index_zero_first = 0
        else:
            index_zero_first = nums.index(0) if 0 in nums else len(nums)
        for i in range(index_zero_first + 1, len(nums)):
            if nums[i] != 0:
                nums[index_zero_first], nums[i] = nums[i], nums[index_zero_first]
                index_zero_first += 1
        return nums
a = Solution()
print(a.moveZeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(a.moveZeroes([0, 0, 1]))  # Output: [1, 0, 0]
print(a.moveZeroes([0, 0, 0]))  # Output: [0, 0, 0]