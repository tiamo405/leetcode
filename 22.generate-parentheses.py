class Solution(object):
    def __init__(self):
        self.ans = []
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
    def fine_print(self, x):
        tmp = ''
        for i in x:
            if i==0 :
                tmp += '('
            else: tmp += ')'
        return tmp
    def binGen(self, x, i, n):
        for j in range(2):
            x[i] = j
            if i == n-1 :
                tmp = self.fine_print(x)
                if self.isValid(tmp):
                    self.ans.append(tmp)
            else :
                self.binGen(x, i+1, n)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        n = n *2
        x = n*[0]
        self.binGen(x, 0, n)
        return self.ans

a = Solution()
print(a.generateParenthesis(16))