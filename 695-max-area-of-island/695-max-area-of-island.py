class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def bfs(point):
            q = deque([point])
            area = 0
            while q:
                curr_x,curr_y = q.popleft()
                area += 1
                for dx,dy in directions:
                    if curr_x + dx >= ROWS or curr_y + dy >= COLS or curr_x + dx < 0 or curr_y+dy < 0 or grid[curr_x+dx][curr_y+dy] == 0:
                        continue
                    grid[curr_x + dx][curr_y + dy] = 0
                    q.append((curr_x+dx,curr_y+dy))
            return area
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    max_area = max(max_area,bfs((r,c)))
                    
        return max_area
                    
            
        