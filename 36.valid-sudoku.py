# AC
class Solution(object):
    def checkArr(self, arr):
        new_arr = []
        for i in arr :
            if i != '.':
                new_arr.append(int(i))
        new_arr = sorted(new_arr)
        for i in range(len(new_arr)-1):
            if new_arr[i] == new_arr[i+1]:
                return False
        return True
    def getCol(self, board, j):
        col = []
        for i in range(9):
            col.append(board[i][j])
        return col
    
    def get_3x3(self, board, i,j):
        arr = []
        for a in range(i, i+3):
            for b in range(j,j+3):
                arr.append(board[a][b])
        return arr
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check hang
        for i in range(9):
            row = []
            for j in range(9):
                row.append(board[i][j])
            if self.checkArr(row) == False:
                return False
         # check cot
        for j in range(9):
            col = self.getCol(board, j)
            if self.checkArr(col) == False:
                return False
        # check 3x3
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                arr = self.get_3x3(board, i, j)
                if self.checkArr(arr) == False:
                    return False
        return True
a = Solution()
print(a.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
