class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        def maxWindowK(minutes):
            alreadySatisfied = 0
            optimal = 0
            
            for i in range(len(grumpy)):
                if grumpy[i] == 0:
                    alreadySatisfied += customers[i]
                    customers[i] = 0
            
            
            current = 0
            for i in range(len(customers)):
                current += customers[i]
                
                if i >= minutes:
                    current -= customers[i - minutes]
                    
                optimal = max(optimal,current)
                    
            return optimal + alreadySatisfied
        
        return maxWindowK(minutes)
        
        
                        
                    
                    
                        
                
                
        