class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r == ROWS or c == COLS or min(r,c) < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            count = 1
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)
            return count


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    count = dfs(r,c)
                    res = max(res, count)

        return res
