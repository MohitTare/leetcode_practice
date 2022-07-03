class Solution:
    def totalFruit(self, fruit: List[int]) -> int:
        dict_fruits = defaultdict(lambda:0)
        l = 0
        for r in range(len(fruit)):
            dict_fruits[fruit[r]] += 1
            if len(dict_fruits) > 2:
                dict_fruits[fruit[l]] -= 1
                if dict_fruits[fruit[l]] == 0: del dict_fruits[fruit[l]]
                l+=1
        return r - l +1
            
                    
                
                
                
    
    
    
                
                
                
            
            
            
        