class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_count = {}
        for num in nums:
            if num in dict_count:
                return num
            else:
                dict_count[num] = 1 