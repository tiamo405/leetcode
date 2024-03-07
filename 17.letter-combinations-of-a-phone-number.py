class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict_digits = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        digits = digits[::-1]
        ans = []
        tmp = []
        for s in digits:
            if len(ans) == 0 :
                for char in dict_digits[s]:
                    ans.append(char)
            else :
                tmp = []
                for char in dict_digits[s]:
                    for st in ans :
                        tmp.append(char+st)
                ans = tmp
        return ans
    
a = Solution()
print(a.letterCombinations("23"))
        