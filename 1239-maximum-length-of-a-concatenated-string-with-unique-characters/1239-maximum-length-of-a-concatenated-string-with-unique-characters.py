class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        
        for item in arr:
            if len(set(item)) < len(item): continue
                
            item  = set(item)
            for comb_item in dp[:]:
                if item & comb_item: continue
                    
                dp.append(item | comb_item)
        
        return max(len(i) for i in dp)
        
                    
                
                
        