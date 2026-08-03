
import math


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # a+b = logarit(e^a * e^b)
        
        return int(math.log(math.exp(a) * math.exp(b)))

a = Solution()
print(a.getSum(-999, 0))