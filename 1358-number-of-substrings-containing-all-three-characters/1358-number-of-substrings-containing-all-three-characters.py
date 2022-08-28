class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        r = 0
        count_map = {'a':0,'b':0,'c':0}
        res = 0
        
        
        for r in range(len(s)):
            count_map[s[r]] += 1
            while all(count_map.values()):
                res += len(s) - r
                count_map[s[l]] -= 1
                l+=1    
        return res
            
                
            
        