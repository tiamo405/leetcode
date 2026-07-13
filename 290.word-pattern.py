class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dict_map = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict_map:
                if words[i] in dict_map.values():
                    return False
                dict_map[pattern[i]] = words[i]
            else:
                if dict_map[pattern[i]] != words[i]:
                    return False
        return True