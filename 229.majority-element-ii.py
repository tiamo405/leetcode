class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        dicts = {}
        for num in nums:
            if num in dicts:
                dicts[num] += 1
            else:
                dicts[num] = 1
        result = []
        for key, value in dicts.items():
            if value > len(nums) // 3:
                result.append(key)
        return result
a = Solution()
print(a.majorityElement([3,2,3,4,4,4]))