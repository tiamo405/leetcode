class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows = rowIndex + 1
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
print(a.getRow(33)) # [1,3,3,1]