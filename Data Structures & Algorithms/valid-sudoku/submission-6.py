class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)

        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c is ".":
                    continue
                if c in cols[j] or c in rows[i] or c in sqs[i//3,j//3]:
                    return False
                
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                sqs[(i//3, j//3)].add(board[i][j])
        return True
                
        