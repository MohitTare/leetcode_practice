class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        
        R = len(grid)
        C = len(grid[0])
        self.res = 0
        
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        
        def dfs(r,c):
            if 0 <= r < R and 0 <= c < C and grid[r][c] == 1:
                grid[r][c] = 0
                self.res += 1
                for dx,dy in dirs:
                    dfs(r + dx, c + dy)
                    
        
     
        for i in range(R):
            for j in range(C):
                if i == 0 or j == 0 or i == R-1 or j == C-1 and grid[i][j] == 1:
                    dfs(i,j)
                    
        
                    
        self.res = 0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    dfs(i,j)
                    
        return self.res
            
            
            
            