class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_nums = {}
        dict_freq = {}
        for num in nums:
            if num in dict_nums:
                dict_nums[num] += 1
            else:
                dict_nums[num] = 1
        for key, value in dict_nums.items():
            if value in dict_freq:
                dict_freq[value].append(key)
            else:
                dict_freq[value] = [key]
        res = []
        print(dict_freq)
        temp_k = k
        while k > 0:
            max_freq = max(dict_freq.keys())
            res += dict_freq[max_freq]
            k -= len(dict_freq[max_freq])
            del dict_freq[max_freq]
        return res[:temp_k]
a = Solution()
print(a.topKFrequent([1,1,1,2,2,3], 2))
print(a.topKFrequent([1], 1))
print(a.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))