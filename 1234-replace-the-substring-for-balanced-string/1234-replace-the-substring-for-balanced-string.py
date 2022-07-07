class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        req_len = len(s) // 4
        l = 0
        res = len(s)
        for r in range(len(s)):
            #print(l,r)
            count[s[r]] -= 1
            
            while l < len(s) and count['Q'] <= req_len and count['W'] <= req_len and count['E'] <= req_len and count['R'] <= req_len:
                res = min(res,r - l + 1)
                count[s[l]] += 1
                l += 1
            
        return res
        