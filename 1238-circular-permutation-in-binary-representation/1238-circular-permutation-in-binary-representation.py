class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def binToGray(n):
            return n ^ (n >> 1)
        
        
        res = list(map(binToGray, range(0, 2 ** n)))
        start_idx = res.index(start)
        return res[start_idx:] + res[:start_idx]
        
        
        
        
        