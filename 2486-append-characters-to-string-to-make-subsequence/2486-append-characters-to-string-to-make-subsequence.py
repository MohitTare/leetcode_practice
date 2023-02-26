class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        s_p = 0
        t_p = 0
        common = 0
        
        while s_p < len(s) and t_p < len(t):
            if s[s_p] == t[t_p]:
                s_p += 1
                t_p += 1
                common += 1
            else:
                s_p += 1
            
        return len(t) - common
    
    
    
    
    