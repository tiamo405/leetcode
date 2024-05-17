class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m,n = len(matrix),len(matrix[0])  
        
        return m,n

a = Solution() 
print(a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # 3,3