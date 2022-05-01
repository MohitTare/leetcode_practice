class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)
        for x,y in points:
            dist = -(y**2 + x**2)
            if len(heap) == k:
                heappushpop(heap,(dist,x,y))
            else:
                heappush(heap,(dist,x,y))
                
        return [[x[1],x[2]] for x in heap]
                    
                    
                
        