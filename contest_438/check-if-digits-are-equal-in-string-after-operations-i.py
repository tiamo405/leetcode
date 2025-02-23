class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s) > 2:
            res = ""
            for i in range(len(s)-1):
                tmp = (int(s[i]) + int(s[i+1])) % 10
                res += str(tmp)
            s = res
        return s[0] == s[1]
    
a = Solution()
print(a.hasSameDigits("3902"))
print(a.hasSameDigits("34789"))
print(a.hasSameDigits("11"))