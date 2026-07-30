class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        if n == 0:
            return 1
        if n == 1:
            return 10
        res = 10
        for i in range(2, n + 1):
            sosohang = 9
            for j in range(2, i+1):
                sosohang *= (10 - j + 1) # có 9 cách chọn số thứ nhất, có 9 cách chọn số thứ 2, cứ thế giảm dần
            res += sosohang
        return res