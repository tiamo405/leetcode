class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dict = {}
        res = []
        for  i in nums :
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for k, v in dict.items():
            if v == 1:
                res.append(k)
        return res
a = Solution()
print(a.singleNumber([1, 2, 1, 3, 2, 5]))
print(a.singleNumber([-1, 0]))