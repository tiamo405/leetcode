class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)==str(x)[::-1]
        x = str(x)
        x_new = x[::-1]
        if x == x_new :return True
        return False