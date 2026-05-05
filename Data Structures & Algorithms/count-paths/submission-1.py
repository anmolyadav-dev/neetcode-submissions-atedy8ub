class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n
        paths = [[0 for i in range(COLS)] for i in range(ROWS)]
        paths[ROWS-1][COLS-1]=1
        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                if r+1<ROWS:

                    paths[r][c]+=paths[r+1][c]
                if c+1< COLS:
                    paths[r][c]+=paths[r][c+1]
        return paths[0][0]
                
