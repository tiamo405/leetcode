class Solution(object):
    def checkDau(self, a, b) :
        if (a == '(' and b ==')') or (a == '{' and b =='}') or (a == '[' and b ==']') :
            return True
        return False
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        moNgoac = '({['
        dongNgoac = ')}]'
        ans = ''
        for i in s :
            if i in moNgoac :
                ans = ans + i
            else :
                if len(ans) == 0:
                    return False
                if self.checkDau(ans[-1], i) :
                    ans = ans [:-1]
                else :
                    return False
        if len(ans)==0 :
            return True
        else :
            return False

a = Solution()
print(a.isValid("]"))