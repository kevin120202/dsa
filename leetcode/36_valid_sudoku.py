class Solution(object):
    def isValidSudoku(self, board):
        # validate rows
        for row in board:
            my_set = set()
            for num in row:
                if num in my_set:
                    return False
                elif num != ".":
                    my_set.add(num)

        # validate cols
        for i in range(9):
            my_set = set()
            for j in range(9):
                if board[j][i] in my_set:
                    return False
                elif board[j][i] != ".":
                    my_set.add(board[j][i])

        # validate boxes
        start_i = [(0, 0), (0, 3), (0, 6),
                   (3, 0), (3, 3), (3, 6),
                   (6, 0), (6, 3), (6, 6)]
        for i in range(len(start_i)):
            my_set = set()
            start, col_start = start_i[i]
            for row in range(start, start + 3):
                for col in range(col_start, col_start + 3):
                    if board[row][col] in my_set:
                        return False
                    elif board[row][col] != ".":
                        my_set.add(board[row][col])
        return True
