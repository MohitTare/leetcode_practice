class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        R = len(grid)
        C = len(grid[0])
        self.max_gold = 0
        
        
        def dfs(point,g,visited):
            curr_x,curr_y = point
            if curr_x < 0 or curr_x >= R or curr_y < 0 or curr_y >= C or grid[curr_x][curr_y] == 0 or (curr_x,curr_y) in visited:
                return g
            
            visited.add((curr_x,curr_y))
            g += grid[curr_x][curr_y]
            
            mx = 0
            for dx,dy in directions:
                mx = max(mx,dfs((curr_x + dx,curr_y + dy),g,visited))
                
            visited.discard((curr_x,curr_y))
            return mx
        
        
        for r in range(0,R):
            for c in range(0,C):
                self.max_gold = max(self.max_gold,dfs((r,c),0,set()))
            
        return self.max_gold
                
                
                
        