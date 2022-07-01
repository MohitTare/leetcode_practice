class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_count = defaultdict(lambda:0)
        l = 0
        max_len = 0
        for r in range(len(s)):
            dict_count[s[r]] += 1
            curr_len = r - l + 1
            if curr_len - max(dict_count.values()) <= k:
                max_len = max(max_len,curr_len)
            else:
                dict_count[s[l]] -= 1
                l+=1
        
        return max_len
        