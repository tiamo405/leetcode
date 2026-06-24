class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tichArr = 1
        result = []
        countZero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                countZero += 1
            else:
                tichArr *= nums[i]
        if countZero > 1:
            return [0] * len(nums)
        elif countZero == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result.append(tichArr)
                else:
                    result.append(0)
        else:
            for i in range(len(nums)):
                result.append(tichArr // nums[i])
        return result

a = Solution()
print(a.productExceptSelf([1, 2, 3, 4]))  #Output: [24, 12, 8, 6]