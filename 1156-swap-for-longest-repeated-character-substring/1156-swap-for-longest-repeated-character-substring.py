class Solution:
    def maxRepOpt1(self, s: str) -> int:
        counter = Counter(s)
        groups = [[ch,len(list(g))] for ch,g in itertools.groupby(s)]
        res = max(min(i + 1,counter[c]) for c,i in groups)
        
        for i in range(1,len(groups) - 1):
            if groups[i-1][0] == groups[i+1][0] and groups[i][1] == 1:
                res = max(res,min(groups[i-1][1] + groups[i+1][1] + 1, counter[groups[i+1][0]]))
                
        return res
            
                
                
                
                
            
        