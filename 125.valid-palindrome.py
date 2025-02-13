class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newS = ''
        for i in range(len(s)):
            if s[i].isalnum():
                newS += s[i]
        return newS.lower() == newS[::-1].lower()

a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))