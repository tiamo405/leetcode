class Solution(object):
    def count_live_neighbors(self, board, row, col, rows, cols):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        live_count = 0

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                live_count += board[r][c]

        return live_count
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        # Create a copy of the original board to keep track of the original state
        copy_board = [[board[i][j] for j in range(cols)] for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                live_neighbors = self.count_live_neighbors(copy_board, i, j, rows, cols)

                # Rule 1 or Rule 3
                if copy_board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 0
                # Rule 4
                elif copy_board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 1