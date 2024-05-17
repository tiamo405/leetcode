class Solution(object):
    def remove_whitespace(self, s):
        for i in range(len(s)):
            a = s[i]
            if a == ' ':
                continue
            elif a =='+' or a=='-' or a.isdigit() :
                return s[i:]
            else:
                return None
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = self.remove_whitespace(s)
        if s is None:
            return 0
        am = 1
        ans = 0
        isDau  = False
        isSo = False
        for i in s :
            if i =='-' or i =='+' :
                if isDau :
                    if isSo :
                        break
                    else:
                        return 0
                if isDau == False:
                    isDau = True
                if i == '-':
                    am = 0
            elif i.isdigit():
                isDau = True
                isSo = True
                ans = ans*10+int(i)
            else :
                break
        if am == 0 : ans = -ans
        ans = max(ans, -2**31)
        ans = min(ans, 2**31-1)
        
        return ans


a = Solution()
print(a.myAtoi("-5-"))
