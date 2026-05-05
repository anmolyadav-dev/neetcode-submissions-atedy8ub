class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n
        def dfs(r,c,dp):
            if r<0 or c<0 or r>=ROWS or c>=COLS:
                return 0
            if r==ROWS-1 and c==COLS-1:
                
                return 1
            if dp[r][c] :
                return dp[r][c]
            dp[r][c] = dfs(r+1,c,dp) + dfs(r,c+1,dp)

            return dp[r][c]
        dp = [[0 for i in range(COLS)] for i in range(ROWS)]
        return dfs(0,0,dp)