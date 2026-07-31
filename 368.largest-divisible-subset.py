class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict_ = {}
        nums.sort()
        for i in range(len(nums)):
            dict_[i] = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dict_[j]) + 1 > len(dict_[i]): # nếu nums[i] chia hết cho nums[j] và độ dài của tập con tại j + 1 lớn hơn độ dài của tập con tại i thì dict_[i] goomf taapj con cua j + theem chinsh nos
                    dict_[i] = dict_[j] + [nums[i]]
        return max(dict_.values(), key=len)