class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        
        i = 0
        j = 0
        
        final = []
        
        
        def compare(f,s):
            #print(f,s)
            l = max(f[0],s[0])
            h = min(f[1],s[1])
            if l > h:
                return []
            else:
                return [l,h]
            
        
        while(i < len(first) and j < len(second)):
            res = compare(first[i],second[j])
            #print(res)
            if len(res) > 0:
                final.append(res)
            
            if first[i][1] <= second[j][1]:
                i+=1
            else:
                j+=1
        
        
        return final
                
            
        
        
        