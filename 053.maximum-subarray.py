class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = int(-1e9)
        sum_ = 0
        for i in range(len(nums)):
            if sum_ + nums[i] > 0:
                sum_ += nums[i]
                res = max(res, sum_)
            else:
                res = max(res, nums[i])
                sum_ = 0
            
        return res

a = Solution() 
print(a.maxSubArray([-2,-1])) # 6