class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        queue = deque()
        
        def bfs(grid,queue,unexploded):
            M = len(grid)
            N = len(grid[0])
            result = 0
            while queue:
                result += 1
                for _ in range(len(queue)):
                    point = queue.popleft()
                    for dx,dy in directions:
                        curr_x,curr_y = point[0] + dx, point[1] + dy
                        if 0 <= curr_x < M and 0 <= curr_y < N and grid[curr_x][curr_y] == 1:
                            unexploded -= 1
                            grid[curr_x][curr_y] = 2
                            queue.append((curr_x,curr_y))

            return result,unexploded


        start = None
        unexploded = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    unexploded += 1
        
        result,unexploded = bfs(grid,queue,unexploded)
        return -1 if unexploded != 0 else max(result-1,0)
        