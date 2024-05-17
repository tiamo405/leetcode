class Solution(object):
    def twoSumclosest(self, nums, target):
        min_d = float('inf')
        ans = None
        left, right = 0, len(nums)-1
        while left < right :
            if nums[left] + nums[right] == target :
                return nums[left] + nums[right]
            elif nums[left] + nums[right] > target :
                if min_d > nums[left] + nums[right] - target : # neu khong cach dc cap nhat
                    ans = nums[left] + nums[right]
                    min_d = nums[left] + nums[right] - target
                right -=1
            else:
                if min_d > target - nums[left] - nums[right] : # neu khong cach dc cap nhat
                    ans = nums[left] + nums[right]
                    min_d = target - nums[left] - nums[right]
                left +=1
        return ans
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        d = float('inf')
        ans = None
        for k in range(len(nums)-2):
            temp_arr = sorted(nums[k+1:])

            min_d = self.twoSumclosest(temp_arr, target-nums[k])
            if d > abs(target - (min_d + nums[k])):
                d = abs(target - (min_d + nums[k]))
                ans = min_d + nums[k]
        return ans

a = Solution()
print(a.threeSumClosest([0,1,2], 3))