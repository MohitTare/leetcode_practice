class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        
        res = []
        
        for i in range(1,len(num)):
            for j in range(i+1,len(num)):
                first = num[:i]
                second = num[i:j]
                remaining = num[j:]
                
                if (first.startswith('0') and first!='0') or  (second.startswith('0') and second!='0'):
                    continue
                res.append(first)
                res.append(second)
                
                while remaining:
                    third = str(int(first) + int(second))
                    if not remaining.startswith(third) or int(third) > 2**31:
                        res = []
                        break
                    res.append(third)
                    remaining = remaining[len(third):]
                    first = second
                    second = third
                
                if not remaining:
                    return res
        
        return []
                    
        