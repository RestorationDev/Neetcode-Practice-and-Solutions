class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #similar to word search solution, will seek "1" vertically or horizontal
        #and recursively keep going until we have an island
        #directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(row_idx, col_idx):
            if (row_idx >= ROWS or col_idx >= COLS or 
            row_idx < 0 or col_idx < 0 or grid[row_idx][col_idx] == "0"):
                return

            #we want to find a way to denote new territory
            #if none of the surrounding indexes are in visited, we are in new territory
            #we also need to make sure we are in bounds...

            grid[row_idx][col_idx] = "0"
            dfs(row_idx + 1, col_idx)
            dfs(row_idx - 1, col_idx)
            dfs(row_idx, col_idx + 1)
            dfs(row_idx, col_idx - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        return count

