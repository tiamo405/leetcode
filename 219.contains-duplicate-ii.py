class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict_index = {}
        for i, num in enumerate(nums):
            if num in dict_index and i - dict_index[num] <= k:
                return True
            dict_index[num] = i
        return False