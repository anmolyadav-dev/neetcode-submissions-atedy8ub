class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r,c,visited,prevHeight):
            if r<0 or c<0 or r>=ROWS or c>=COLS:
                return
            dir = [[1,0],[-1,0],[0,1],[0,-1]]
            if (r,c) in visited:
                return
            if heights[r][c]<prevHeight: return
            visited.add((r,c))
            for dr,dc in dir:
                nr = r + dr
                nc = c+ dc
                if 0<=nr<ROWS and 0<=nc<COLS:    
                    dfs(nr,nc,visited,heights[r][c])
            
        
        for i in range(0,COLS):
            dfs(ROWS-1,i,atlantic,heights[ROWS-1][i])
            dfs(0,i,pacific,heights[0][i])
        for i in range(0,ROWS):
            dfs(i,0,pacific,heights[i][0])
            dfs(i,COLS-1,atlantic,heights[i][COLS-1])
        # print(pacific,atlantic)
        res = []
        for el in pacific:
            if el in atlantic:
                res.append(el)
        return res