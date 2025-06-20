class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_bin = ''
        while n > 0:
            str_bin = str(n % 2) + str_bin
            n //= 2
        return str_bin.count('1')
a = Solution()
print(a.hammingWeight(11))  # Output: 3
print(a.hammingWeight(2147483645))  # Output: 30
