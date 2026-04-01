class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #we must begin with the start letter, if there's no start letter adjacencies,
        #return false
        
        def dfs(i, j, lsf):
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != word[lsf]:
                return False
            if lsf == len(word) - 1:
                return True
            
            temp = board[i][j]
            board[i][j] = '#'

            found = (dfs(i + 1, j, lsf + 1) or
            dfs(i, j + 1, lsf + 1) or
            dfs(i - 1, j, lsf + 1) or
            dfs(i, j - 1, lsf + 1))

            board[i][j] = temp

            return found
            #we want our dfs to check all surrounding pieces, marking them # as visited

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
