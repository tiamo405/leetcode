class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        len1 = len(version1)
        len2 = len(version2)
        for i in range(max(len1, len2)):
            v1 = int(version1[i]) if i < len1 else 0
            v2 = int(version2[i]) if i < len2 else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
a = Solution()
print(a.compareVersion("1.2", "1.10")) # -1
print(a.compareVersion("1.01", "1.001")) # 0
print(a.compareVersion("1.0", "1.0.0.0")) # 0