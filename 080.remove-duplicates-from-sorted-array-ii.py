class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        countDup = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                countDup = 1
                count += 1
            elif nums[i] == nums[i-1] and countDup == 1:
                countDup += 1
                count += 1 
            elif nums[i] == nums[i-1] and countDup >= 2:
                continue
        return count
a = Solution()
print(a.removeDuplicates([1,1,1,2,2,3])) # 5
