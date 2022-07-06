class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        count_map = {c:0 for c in 'abc'}
        l = 0
        count = 0
        for r in range(len(s)):
            count_map[s[r]] += 1
            while all(count_map.values()):
                count_map[s[l]] -= 1
                l+=1
            count += l
            
        return count
        