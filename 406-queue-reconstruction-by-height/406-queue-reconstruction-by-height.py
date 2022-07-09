class Solution:
    def reconstructQueue(self, p: List[List[int]]) -> List[List[int]]:
        res = []
        stack = []
        p.sort(key=lambda p: (-p[0],p[1]))
        for i in p:
            res.insert(i[1],i)
            
        return res
        
            
            
        
        
        