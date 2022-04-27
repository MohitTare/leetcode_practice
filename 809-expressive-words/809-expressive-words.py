class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check(S, W):
            i, j, i2, j2, n, m = 0, 0, 0, 0, len(S), len(W)
            while i < n and j < m:
                if S[i] != W[j]: return False
                while i2 < n and S[i2] == S[i]: i2 += 1 # increment 2nd pointer till end of group for stretchy characters
                while j2 < m and W[j2] == W[j]: j2 += 1
                if i2 - i != j2 - j and i2 - i < max(3, j2 - j): return False # Source group must be 3 or more characters
                i, j = i2, j2
            return i == n and j == m
        
        
        result = 0
        for w in words:
            if check(s,w):
                result += 1
                
        return result
