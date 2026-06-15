class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()

        def addCell(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] != 1:
                return
            queue.append([r,c])
            visit.add((r,c))

        # Get all cells with rotten fruit & add to Queue
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh +=1

        time = 0
        while queue:
            rotting = False
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    rotting = True
                    fresh -= 1
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)

            if rotting:
                time += 1            

        return time if fresh == 0 else -1

        # BFS from all rotten fruit
        # BFS search from all at the same time

        # need to convert the good fruit to rotten 