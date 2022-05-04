class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Basic trick here is winlen <= max no of repeating characters + k
        l = 0
        max_len = 0
        freq = defaultdict(lambda:0)
        for r in range(len(s)):
            freq[s[r]] += 1
            win_len = r - l + 1
            if win_len - max(freq.values()) <= k:
                max_len = max(max_len,win_len)
            else:
                freq[s[l]] -= 1
                l += 1
        return max_len
            
            
            
        
        
                
        