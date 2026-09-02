from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                curr = board[i][j]
                if curr in rows[i] or curr in cols[j] or curr in squares[(i//3, j//3)]:
                   return False
                rows[i].add(curr)
                cols[j].add(curr)
                squares[(i//3, j//3)].add(curr)

        return True