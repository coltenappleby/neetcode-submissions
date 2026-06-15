from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(start_r, start_c):

            queue = deque([(start_r, start_c, 0)])
            visited = {(start_r,start_c)}

            while queue:
                r, c, d = queue.popleft()

                if grid[r][c] > d:
                    grid[r][c] = d

                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = r + dr, c + dc

                    if ( min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == -1 or (grid[nr][nc] == 0 and d > 0) or
                        (nr, nc) in visited):
                        continue

                    visited.add((nr,nc))
                    queue.append((nr, nc, d+1))
        
        for R in range(ROWS):
            for C in range(COLS):
                if grid[R][C] == 0:
                    bfs(R,C)
            