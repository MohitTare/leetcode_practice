class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        R = len(grid)
        C = len(grid[0])
        
        visited = {(0,0): grid[0][0]}
        
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        steps = 0
        
        q = deque([(0,0,0)])
        
        while q:
            size = len(q)
            for _ in range(size):
                curr_x,curr_y,curr_obs = q.popleft()
                if curr_obs > k:
                    continue

                if curr_x == R - 1 and curr_y == C - 1:
                    return steps

                for dx,dy in directions:
                    new_r = curr_x + dx
                    new_c = curr_y + dy

                    if 0 <= new_r < R and 0 <= new_c < C:
                        new_obs = curr_obs +  1 if grid[new_r][new_c] == 1 else curr_obs
                        if new_obs < visited.get((new_r,new_c), float('inf')):
                            visited[(new_r,new_c)] = new_obs
                            q.append((new_r,new_c,new_obs))

            steps += 1
            
        return -1
                    
                    
                    
            