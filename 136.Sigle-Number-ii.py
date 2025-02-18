class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dem = {}
        for i in nums:
            if i in dem:
                dem[i] +=1
            else:
                dem[i] = 1
        for key, value in dem.items():
            if value == 1:
                return key
a = Solution()
print(a.singleNumber([2,2,1,2])) # 1