class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        # function is used to add all surrounding cells, starting at gate
        # handle for keeping in bounds, avoiding water, not revisiting...
        # finally added to queue...
        def addRoom(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or 
            (r,c) in visit or grid[r][c] == -1):
                return
            
            visit.add((r,c))
            q.append([r,c])

        #this block handles adding queues for each treasure,
        # since a multi bfs approach is more efficient
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r, c))
        
        #we essentially keep adding surrounding rooms
        #distance should increase 1 by 1...
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1

