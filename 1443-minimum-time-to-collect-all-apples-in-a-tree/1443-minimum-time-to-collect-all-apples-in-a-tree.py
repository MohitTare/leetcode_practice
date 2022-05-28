class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        adj = defaultdict(list)
        
        visited = set()
        
        for e,v in edges:
            adj[e].append(v)
            adj[v].append(e)
        
        total_cost = [0]
        
        def dfs(node):
            found = False
            visited.add(node)
            
            for nxt in adj[node]:
                if nxt in visited:
                    continue
                if dfs(nxt):
                    found = True
                    total_cost[0] += 2
            
            return found or hasApple[node]
        
        
        dfs(0)
        return total_cost[0]
            