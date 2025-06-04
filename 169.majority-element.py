class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        count = 0 
        temp = nums[0]
        for num in nums:
            if num == temp:
                count += 1
            else:
                count = 1
                temp = num
            if count > len(nums) // 2:
                return num
        return None
a = Solution()
print(a.majorityElement([3,2,3])) # 3
