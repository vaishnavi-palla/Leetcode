class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for i in row:
                if i in seen and i != ".":
                    return False
                seen.add(i)
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] in seen and board[j][i] != ".":
                    return False
                seen.add(board[j][i])

            for row in range(0, 9, 3):
                for col in range(0, 9, 3):
                    seen = set()
                    for i in range(3):
                        for j in range(3):
                            cell = board[row + i][col + j]
                            if cell in seen and cell != ".":
                                return False
                            seen.add(cell)
        return True
