class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))
a = Solution()
print(a.reverseWords("the sky is blue")) # "blue is sky the"
print(a.reverseWords("  hello world!  ")) # "world! hello"