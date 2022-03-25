class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], M: int, L: int) -> int:
        prefix = [0]
        maxl = maxm = summ = 0
        for x in A:
            prefix.append(prefix[-1] + x)
        
        for x in range(M, len(prefix) - L):
            maxm = max(maxm, prefix[x] - prefix[x - M])
            summ = max(summ, maxm + prefix[x + L] - prefix[x])
        
        for x in range(L, len(prefix) - M):
            maxl = max(maxl, prefix[x] - prefix[x - L])
            summ = max(summ, maxl + prefix[x + M] - prefix[x])
        
        return summ
            
            
        
        
        