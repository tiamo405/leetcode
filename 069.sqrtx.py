class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxNum = 2**16
        for i in range(maxNum):
            if i*i > x:
                return i-1
            