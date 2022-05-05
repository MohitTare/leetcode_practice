class Solution:
    def countPairs(self, foods: List[int]) -> int:
        num_powers = [2**x for x in range(22)]
        res = 0
        freq_count = defaultdict(int)
        
        for f in foods:
            for power in num_powers:
                res += freq_count[power - f]
            freq_count[f] += 1
        
        return res % (10**9 + 7)
        
        
        
            
                
                
        
        
        
        