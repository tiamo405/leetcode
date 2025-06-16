class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        adns = {}
        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            if seq in s[i+1:]:
                if seq not in adns:
                    adns[seq] = 2
                    i += 9  # Skip the next 9 characters to avoid counting the same sequence again
                # else:
                #     adns[seq] += 1
        return [seq for seq, count in adns.items() if count > 1]

a = Solution()
print(a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(a.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
