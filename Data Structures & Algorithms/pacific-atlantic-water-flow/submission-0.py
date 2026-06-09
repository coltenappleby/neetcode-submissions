class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific: r < 0 and c < 0
        # atlantic: r >= len(heights) and c >= len(heights[0])

        pacific = set()
        atlantic = set()

        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r,c, prev_height, ocean):
            if r < 0 or c < 0:
                return
            if r == ROWS or c == COLS:
                return

            if (r,c) in ocean:
                return

            height = heights[r][c]

            if height >= prev_height:
                ocean.add((r,c))

                dfs(r+1, c, height, ocean)
                dfs(r-1, c, height, ocean)
                dfs(r, c+1, height, ocean)
                dfs(r, c-1, height, ocean)
            

        # ds for starting cells
        for r in range(ROWS):
            dfs(r, 0, 0, pacific)
            dfs(r, COLS-1, 0, atlantic)

        for c in range(COLS):
            dfs(0, c, 0, pacific)
            dfs(ROWS-1, c, 0, atlantic)


        # find intersection from pacific and atlantic
        res = []
        for coord in pacific:
            if coord in atlantic:
                res.append([coord[0], coord[1]])

        return res

        
            

            

            


                