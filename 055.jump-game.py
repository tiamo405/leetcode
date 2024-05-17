class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = 0
        if index + nums[index] >= len(nums)-1:
            return True
        while index < len(nums)-1:
            if index + nums[index] >= len(nums) - 1:
                return True
            
            max_val = nums[index] + index
            tmp = max_val
            for i in range(index+1, index + nums[index]+1):
                if max_val < i + nums[i]:
                    max_val = max(max_val, i + nums[i])
                    index = i
            if max_val == tmp: # khong thay doi, index ban dau lon nhat roi
                return False

a = Solution()
print(a.canJump([0])) # false