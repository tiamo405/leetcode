class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        for i in range(0, len(haystack)-n+1):
            tmp = haystack[i:i+n]
            if tmp == needle:
                return i
        return -1