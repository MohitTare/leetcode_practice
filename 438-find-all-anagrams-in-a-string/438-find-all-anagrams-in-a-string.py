class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        t_count = Counter(p)
        s_count = {c:0 for c in t_count.keys()}
        curr_wind= len(p)
        l = 0
        res = []
        for r in range(len(s)):
            #print(l,r,s_count)
            if s[r] in t_count.keys():
                s_count[s[r]] += 1
            
            while  (r - l + 1) >= curr_wind:
                if s_count == t_count:
                    res.append(l)
                if s[l] in t_count.keys():
                    s_count[s[l]] -= 1
                l+=1
        return res                    
                
                
                    
            
            

            
        
        