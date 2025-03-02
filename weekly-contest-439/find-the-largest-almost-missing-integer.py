class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # ©leetcode
        # dict_nums cho tat ca = 0
        dict_nums = {}

        for i in range(0, len(nums)-k+1):
            arr_sub = nums[i:i+k]
            arr_tmp = []
            for num in arr_sub:
                if num not in dict_nums:
                    dict_nums[num] = 1
                    arr_tmp.append(num)
                else:
                    if num not in arr_tmp:
                        dict_nums[num] +=1
        res = -1
        # check all key in dict lay max if value = 1
        for key, value in dict_nums.items():
            if value == 1:
                res = max(res, key)
        return res
a = Solution()
print(a.largestInteger([3,9,2,1,7],3))
print(a.largestInteger([3,9,7,2,1,7],4))
print(a.largestInteger([0,0],1))
print(a.largestInteger([0,0],2))

