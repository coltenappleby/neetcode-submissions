class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        global_visit = set()
        

        def dfs(start_r, start_c):
            stack = [(start_r, start_c)]
            visit = set(())
            valid = True

            while stack:
                r, c = stack.pop()
                if r == 1 and c == 1:
                    print((r,c, board[r][c], (r,c) in global_visit, (r,c) in visit))
                if (r,c) in global_visit:
                    continue
                if min(r,c) < 0 or r == ROWS or c == COLS:
                    
                    valid = False
                    continue
                    # break
                global_visit.add((r,c))
                visit.add((r,c))
         
                if  board[r][c] == 'X':
                    continue

                # I dont think we need to go up or to the left
                stack.append((r+1, c))
                stack.append((r-1, c))
                stack.append((r, c+1))
                stack.append((r, c-1))

            if valid:
                for r,c in visit:
                    board[r][c] = 'X'
            return


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in global_visit:
                    dfs(r,c)