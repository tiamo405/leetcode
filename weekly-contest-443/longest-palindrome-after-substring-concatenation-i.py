class Solution(object):
    def isPalindrome(self, s):
        return s == s[::-1]
    def longestPalindrome(self, s, t):

        def get_palindromes(string):
            n = len(string)
            palindromes = set()
            
            # Expand Around Center
            for center in range(n):
                # Odd-length palindromes
                l, r = center, center
                while l >= 0 and r < n and string[l] == string[r]:
                    palindromes.add(string[l:r+1])
                    l -= 1
                    r += 1

                # Even-length palindromes
                l, r = center, center + 1
                while l >= 0 and r < n and string[l] == string[r]:
                    palindromes.add(string[l:r+1])
                    l -= 1
                    r += 1
            
            return palindromes

        s_palindromes = get_palindromes(s)
        t_palindromes = get_palindromes(t)

        max_length = 0
        # Check all combinations
        for sp in s_palindromes:
            for tp in t_palindromes:
                combined = sp + tp
                if combined == combined[::-1]:  # Check palindrome
                    max_length = max(max_length, len(combined))

        return max_length

a = Solution()
print(a.longestPalindrome("a", "a"))
print(a.longestPalindrome("abc", "def"))
print(a.longestPalindrome("b", "aaaa"))
print(a.longestPalindrome("abcde", "ecdba"))
print(a.longestPalindrome("kz", "z"))