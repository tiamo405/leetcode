class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        res.append([1])
        for i in range(1, numRows):
            len_row = i+1
            tmp = [] 
            for j in range(len_row):
                if j == 0 or j == len_row-1:
                    tmp.append(1)
                else:
                    tmp.append(res[i-1][j-1] + res[i-1][j]) 
            res.append(tmp)
        return res[-1]
a = Solution()
print(a.generate(5)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]