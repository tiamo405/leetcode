class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums) + 1) // 2
        left = nums[:mid][::-1]
        right = nums[mid:][::-1]
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = left[i // 2]
            else:
                nums[i] = right[i // 2]
        return nums