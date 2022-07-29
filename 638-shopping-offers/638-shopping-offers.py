class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], finalneeds: List[int]) -> int:
        self.min_cost = sum([price[i] * x for i, x in enumerate(finalneeds)])
        
        
        def dfs(offer_list,curr_price,needs):
            if sum(needs) == 0:
                self.min_cost = min(self.min_cost,curr_price)
                return
            
            for offer in offer_list:
                valid = True
                for j,item in enumerate(needs):
                    if item - offer[j] < 0:
                        valid = False
                        break
                if valid:
                    dfs(offer_list,curr_price + offer[-1],[item - offer[j] for j,item in enumerate(needs)])
                
            if sum(needs) > 0:
                for k,item in enumerate(needs):
                    curr_price += price[k] * item
                self.min_cost = min(self.min_cost,curr_price)
                
        
        dfs(special,0, finalneeds)
        return self.min_cost
                
                
                
            
                
                
                
                
        
        
        
        