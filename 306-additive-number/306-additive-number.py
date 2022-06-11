class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1,len(num)):
            for j in range(i+1, len(num)):
                first = num[:i]
                second = num[i:j]
                remaining = num[j:]
                
                if first.startswith('0') and first != '0':
                    continue
                    
                if second.startswith('0') and second != '0':
                    continue
                
                
                while remaining:
                    third = str(int(first) + int(second))
                    if not remaining.startswith(third):
                        break
                    
                    first = second
                    second = third
                    remaining  = remaining[len(third):]
                    
                
                if not remaining:
                    return True
        
        return False
                
        
        
            
        