class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num_str = [str(num) for num in nums]
        for i in range(len(num_str)):
            for j in range(i + 1, len(num_str)):
                if num_str[i] + num_str[j] < num_str[j] + num_str[i]:
                    num_str[i], num_str[j] = num_str[j], num_str[i]
        result = ''.join(num_str)
        return result if result[0] != '0' else '0'
# Example usage:
a = Solution()
print(a.largestNumber([3, 30, 34, 5, 9]))