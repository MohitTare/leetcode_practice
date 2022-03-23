class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        e_cnt = Counter(p)
        a_cnt  = Counter(s[:len(p) - 1])
        res = []
        for i in range(len(p) - 1, len(s)):
            a_cnt[s[i]] += 1
            if e_cnt == a_cnt:
                res.append(i- len(p) + 1)
            a_cnt[s[i - len(p) + 1]] -= 1
            if  a_cnt[s[i - len(p) + 1]] == 0:
                del a_cnt[s[i - len(p) + 1]]
        return res
            
            
        
        