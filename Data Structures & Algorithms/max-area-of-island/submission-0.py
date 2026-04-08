class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if min(r,c)<0 or r>=len(grid) or c>= len(grid[0]):
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            
            walk = [(0,1),(0,-1),(-1,0),(1,0)]
            for nr , nc in walk:
                area += dfs(r+nr,c+nc)
                
            return area

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res= max(dfs(r,c),res)
                    
        return res