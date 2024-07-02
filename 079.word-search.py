class Solution(object):
    def dfs(self,board,word,i,j):
        if len(word) == 0:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp,board[i][j] = board[i][j],'#' # '#' is a marker to avoid visiting the same cell again
        res = self.dfs(board,word[1:],i+1,j) or self.dfs(board,word[1:],i-1,j) or self.dfs(board,word[1:],i,j+1) or self.dfs(board,word[1:],i,j-1)
        board[i][j] = tmp
        return res
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row,col = len(board),len(board[0])
        for i in range(row):
            for j in range(col):
                if self.dfs(board,word,i,j):
                    return True
        return False
    
a = Solution()
print(a.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")) # True