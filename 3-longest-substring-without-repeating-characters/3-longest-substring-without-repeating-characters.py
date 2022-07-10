class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = defaultdict(lambda:0)
        res = 0
        #if len(s) == 1:
        #    return 1
        for r in range(len(s)):
            count[s[r]] += 1
            while max(count.values()) > 1:
                count[s[l]] -= 1
                if count[s[l]] == 0: del count[s[l]]
                l += 1
            res = max(res,r - l + 1)
        return res
        