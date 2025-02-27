class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < res:
                return nums[i]
        return res
a = Solution()
print(a.findMin([3,4,5,1,2])) # 1