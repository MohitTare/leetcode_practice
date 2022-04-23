class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # BFS + maintain distance array to update the distance only if a shorter path is found
        graph = defaultdict(list)
        
        for e1,e2,w in times:
            graph[e1].append((e2,w))
        
        elapsed_time = [0] + [float('inf')] * n
        queue = deque([(0,k)])

        def bfs():
            while queue:
                t,curr = queue.popleft()
                if t < elapsed_time[curr]:
                    elapsed_time[curr] = t
                    for v,w in graph[curr]:
                        queue.append((t+w,v))
                        
       
        bfs()
        result = max(elapsed_time)
        return result if result < float('inf') else -1
                    
                
        
        
        