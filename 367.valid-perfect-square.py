class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x_sqrt = 1
        while x_sqrt * x_sqrt < num:
            x_sqrt += 1
        return x_sqrt * x_sqrt == num