class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        index_zero = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    index_zero.append((i,j))
        for i in index_zero:
            x,y = i
            for j in range(n):
                matrix[x][j] = 0
            for j in range(m):
                matrix[j][y] = 0
        return matrix
a = Solution()
print(a.setZeroes([[1,1,1],[1,0,1],[1,1,1]])) # [[1,0,1],[0,0,0],[1,0,1]]