
from collections import defaultdict

class Solution:
    def getSignature(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        return ''.join(result)

    def groupAnagrams(self, strs):
        result = []
        groups = defaultdict(list)

        for s in strs:
            groups[self.getSignature(s)].append(s)

        result.extend(groups.values())

        return result

a = Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["eat","tea","ate"],["tan","nat"],["bat"]]