class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==1 :
            if nums[0] == target :
                return 0
            return -1
        index_rotate = -1
        index_target = -1
        # for i in range(len(nums)-1):
        #     if nums[i]> nums[i+1]:
        #         index_rotate = i
        #     if nums[i]== target :
        #         index_target = i
        # if nums[-1] == target :
        #     index_target = len(nums)-1
        # if index_target == -1:
        #     return -1
        # if index_rotate == -1:
        #     return index_target
        # if index_target > index_rotate:
        #     return index_target - index_rotate -1
        # else :
        #     return len(nums) - index_rotate + index_target
        for i in range(len(nums)):
            if nums[i] == target :
                return i
        return -1
# AC