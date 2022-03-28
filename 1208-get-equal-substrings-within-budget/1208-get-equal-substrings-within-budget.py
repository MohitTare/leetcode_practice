class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        max_len =0 
        l = 0
        cost_array = deque()
        r = 0
        while(r < len(s)):
            if s[r] != t[r]:
                if max_cost - abs(ord(s[r])- ord(t[r])) >= 0:
                    max_cost -= abs(ord(s[r])- ord(t[r]))
                    cost_array.append(abs(ord(s[r])- ord(t[r])))
                    max_len = max(max_len,r - l + 1)
                    r += 1
                else:
                    if len(cost_array) > 0 and s[l] != t[l]:
                        first_diff = cost_array.popleft()
                        max_cost += first_diff
                        l+=1
                    elif len(cost_array) > 0 and s[l] == t[l]:
                        l += 1
                    else:
                        l+=1
                        r+=1
            else:
                max_len = max(max_len,r - l + 1)
                r+=1
        return max_len
        