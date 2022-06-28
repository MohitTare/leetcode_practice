class Solution:
    def minimumLength(self, s: str) -> int:
        res = len(s)
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                ch = s[l]
                while l < len(s) and s[l] == ch:
                    l += 1
                while r >= 0 and s[r] == ch:
                    r -= 1
                res = len(s[l:r+1])
            else:
                return res
            
        return res
        