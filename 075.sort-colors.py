class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dem = [0,0,0]
        for i in nums:
            dem[i] += 1
        res = []
        for i in range(3):
            res += [i]*dem[i]
        for i in range(len(nums)):
            nums[i] = res[i]
        return nums
a = Solution()
print(a.sortColors([2,0,2,1,1,0])) # [0,0,1,1,2,2]