class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # convert left and right to binary strings
        left_bin = bin(left)[2:]
        right_bin = bin(right)[2:]
        # find the length of the shorter binary string
        min_length = min(len(left_bin), len(right_bin))
        res = right_bin[:len(right_bin) - min_length]
        for i in range(len(left_bin)):
            if left_bin[i] == right_bin[len(right_bin) - min_length + i]:
                res += '1'
            else:
                res += '0'
        return int(res, 2)
a = Solution()
print(a.rangeBitwiseAnd(5, 7))  # Output: 4
print(a.rangeBitwiseAnd(0, 0))  # Output: 0
print(a.rangeBitwiseAnd(1, 2147483647))  # Output: 0