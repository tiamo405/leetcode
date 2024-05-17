class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        index = 0
        step = 0
        if nums[index] == n:
            return 0
        if index + nums[index] >= n:
            return 1
        while index < n-1:
            if index + nums[index] >= n - 1:
                step += 1
                return step
            max_val = nums[index]
            for i in range(index+1, index + nums[index]+1):
                if max_val < i + nums[i]:
                    max_val = max(max_val, i + nums[i])
                    index = i
            step += 1
        return step
    
a = Solution()
print(a.jump([1]))