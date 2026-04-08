class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        totalRows= len(board)
        totalCols = len(board[0])
        
        def dfs(r,c,curWord,visited):
            if min(r,c)<0 or r==totalRows or c == totalCols or (r,c) in visited:
                return False
            curWord = curWord + board[r][c]
            if curWord == word:
                return True
            if curWord not in word:
                return False
            visited.add((r,c))

            # right
            
            right = dfs(r,c+1,curWord,visited)
            # down
            down =dfs(r+1,c,curWord,visited)
            # left
            left =dfs(r,c-1,curWord,visited)
            # up
            up =dfs(r-1,c,curWord,visited)
            
            visited.remove((r,c))
            return right or down or left or up
        startidx = []
        for r in range(totalRows):
            for c in range(totalCols):
                if board[r][c] == word[0]:
                    
                    startidx.append((r,c))
        ans = 0
        for r,c in startidx:
            if dfs(r,c,"",set()):
                return True
        
        return False