class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        #denotes cells that reach pac and atl respectively
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # we don't run if it's out of bounds or if it has already been visited
            # we also don't run if the heights are decreasing from perspective of ocean

            if ((r,c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return

            #add each valid one to set 
            visit.add((r,c))

            #check all surrounding neighbors via dfs
            dfs(r + 1,c, visit, heights[r][c])
            dfs(r - 1,c, visit, heights[r][c])
            dfs(r ,c + 1, visit, heights[r][c])
            dfs(r,c - 1, visit, heights[r][c])

        #this loop finds us all the valid pacific oceans entries
        # (where pac is visit in dfs)
        for c in range(COLS):
            dfs(0,c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])
        #this loop finds us all the valid atlantic oceans entires
        # (where atl is visit in dfs)
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        #lastly, all cells that are in both pac and atl are added to res
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res