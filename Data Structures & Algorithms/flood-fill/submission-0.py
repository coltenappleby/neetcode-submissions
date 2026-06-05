class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if color == original_color:
            return image

        print(original_color)

        # never have to visit a space more than once, might not matter
        # common dfs algo 
        # if color is oringial color, change it and move on.
        # we dont need to track if we have visited a space since we process these in order, and are
        #   constantly updating the color. if it doesnt match the color of the original, stop recursing

        def dfs(grid, r, c):
            ROWS, COLS = len(grid), len(grid[0])
            print(r,c)
            if (min(r,c)) < 0 or r == ROWS or c == COLS or grid[r][c] != original_color:
                return grid
            grid[r][c] = color
            
            grid = dfs(grid, r+1, c)
            grid = dfs(grid, r-1, c)
            grid = dfs(grid, r, c+1)
            grid = dfs(grid, r, c-1)

            return grid

        grid = dfs(image, sr, sc)
        return grid
            