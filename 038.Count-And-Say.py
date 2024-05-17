# AC
class Solution(object):
    def say(self, s):
        count  = 0
        tmp = ''
        ans = ''
        for i in s:
            if tmp == '':
                tmp = i
                count += 1
            elif i == tmp:
                count += 1
            else:
                ans += str(count) + tmp
                tmp = i
                count = 1
        return ans + str(count) + tmp
        
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n ==1 :
            return '1'
        return self.say(self.countAndSay(n-1))
a = Solution()
print(a.countAndSay(4))