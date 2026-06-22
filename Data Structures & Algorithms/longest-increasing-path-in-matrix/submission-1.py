class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[0 for i in range(COLS+1)] for j in range(ROWS+1)]
        def dfs(r,c):
            # base condn
            if r>=ROWS or c>=COLS or r<0 or c<0:
                return 0
            if dp[r][c]:
                return dp[r][c]
            dir = [[1,0],[-1,0],[0,-1],[0,1]]
            arr = [0,0,0,0]
        
        
            # main condn
            ans =1
            for dr,dc in dir:
                nr = r+dr
                nc = c+dc
                if 0<=nr<ROWS  and 0<=nc<COLS:
                    if matrix[r][c]<matrix[nr][nc]:
                        ans = max(ans,1+dfs(nr,nc))
            dp[r][c]=ans
            return dp[r][c]
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(dfs(r,c),res)
        return res
        