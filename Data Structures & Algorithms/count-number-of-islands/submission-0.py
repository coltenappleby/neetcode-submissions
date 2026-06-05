class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        count = 0
        
        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] != '1':
                return

            # (1) find all the ones that are connected and change them to 1,
            # (2) Then go and find the next 1s. we need to know if we are coming from water or land
            
            grid[r][c] = '0'
                

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r,c)
        return count
            
             
