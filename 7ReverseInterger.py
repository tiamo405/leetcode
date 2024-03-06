class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        am = 1
        if x <0 :
            am = 0
            s = str(x)[1:]
        s = s[::-1]
        ans = 0
        for i in s :
            ans = ans*10+int(i)
        if am ==0 :
            ans = -ans
        if ans < -2**31 or ans > 2**31-1:
            return 0
        return ans


a= Solution()
print(a.reverse(1534236469))