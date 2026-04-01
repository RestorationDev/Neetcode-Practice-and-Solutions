class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row must contain all 1-9, no dupes
        #col same
        #sq same
        #find a way to correspond positions between rows, cols, and sqs


        #PLAN:
        #iterate through r,c
        #throw out any blank values, unnecessary
        #check 3 things, if in resp row alr, if in resp col alr, in resp box alr
        #if so, return false
        #otherwise, add into each at set at specified key
        #must do a division by 3 using some array math
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)

        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c is ".":
                    continue
                if c in cols[j] or c in rows[i] or c in sqs[(i//3, j//3)]:
                    return False
                
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                sqs[(i//3, j//3)].add(board[i][j])
        
        return True
            
