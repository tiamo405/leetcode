class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res =  ['0'*n]
        def backtrack(path):
            if len(res) == 2**n:
                return
            for i in range(n-1, -1, -1):
                if path[i] == '0':
                    tmp = list(path)
                    tmp[i] = '1'
                    res.append(''.join(tmp))
                    backtrack(''.join(tmp))
                else:
                    
        backtrack('0'*n)
        return res
a = Solution()
print(a.grayCode(3)) # [0,1,3,2]