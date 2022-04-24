class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for i,keys in enumerate(rooms):
            graph[i].extend(keys)
            
            
            
        visited = set()
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for n in graph[node]:
                    dfs(n)
                    
        dfs(0)
        return len(visited) == len(rooms)
                    
        
        
        
        
        