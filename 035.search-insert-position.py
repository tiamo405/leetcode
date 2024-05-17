class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index= len(nums)

        if nums[0]>= target : return 0
        for i in range(len(nums)):
            if nums[i]==target :
                return i
            elif nums[i]< target:
                if i == len(nums)-1:
                    return i+1
                if nums[i+1] > target :
                    return i+1
        
# AC