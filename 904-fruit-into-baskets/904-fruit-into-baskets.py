class Solution:
    def totalFruit(self, fruit: List[int]) -> int:
        fruitd = defaultdict(lambda:0)
        l = 0
        count = 0
        for r in range(len(fruit)):
            fruitd[fruit[r]] += 1
            count += 1
            if len(fruitd) > 2:
                fruitd[fruit[l]] -= 1
                if fruitd[fruit[l]] == 0: del fruitd[fruit[l]]
                l+=1
        return r-l+1
                
        
                
                
                
            
            
            
        