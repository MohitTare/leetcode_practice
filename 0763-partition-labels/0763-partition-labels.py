class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        dict_pos = {}
        res = []
        
        for i in range(len(s)):
            dict_pos[s[i]] = max(dict_pos.get(s[i],0),i)
            
        
        l = 0
        r = 0
        
        curr_map = set()
        
        for r in range(len(s)):
            curr_map.add(s[r])
            if r >= max(dict_pos[c] for c in curr_map):
                curr_map = set()
                res.append(r - l + 1)
                l=r+1
                
        return res
                
                
            
            
        